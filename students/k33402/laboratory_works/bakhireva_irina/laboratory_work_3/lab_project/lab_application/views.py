from django.db.models import Q, Max
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, exceptions
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from lab_application.models import *
from lab_application.serializers import FullSpecializationSerializer, ShortVacancySerializer, FullVacancySerializer, \
	FullApplicantSerializer, EditApplicantSerializer, CourseSerializer, ShortCompanySerializer, \
	FullCompanyAndVacanciesSerializer, ShortVacancyWithoutCompanySerializer, CreateVacancySerializer, \
	EditVacancySerializer, ShortApplicantSerializer

specialization = openapi.Parameter('specialization', openapi.IN_QUERY,
                                   description="Фильтр вывода по требуемой профессии",
                                   type=openapi.TYPE_INTEGER)


class SpecializationsListView(generics.ListAPIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]
	queryset = Specialization.objects.all()
	serializer_class = FullSpecializationSerializer


class CoursesListView(generics.ListAPIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]
	serializer_class = CourseSerializer

	def get_queryset(self):
		queryset = Course.objects.all()
		if "specialization" in self.request.GET:
			queryset = queryset.filter(spec=self.request.GET["specialization"])
		return queryset

	@swagger_auto_schema(manual_parameters=[specialization])
	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)


class CompaniesListView(generics.ListAPIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]
	queryset = Company.objects.all()
	serializer_class = ShortCompanySerializer


class CompanyView(generics.RetrieveAPIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]
	queryset = Company.objects.all()
	serializer_class = FullCompanyAndVacanciesSerializer


class VacanciesListView(generics.ListAPIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]
	serializer_class = ShortVacancySerializer

	def get_queryset(self):
		queryset = Vacancy.objects.filter(closed_date=None)
		if "specialization" in self.request.GET:
			queryset = queryset.filter(specs__id=self.request.GET["specialization"]).distinct()
		return queryset

	@swagger_auto_schema(manual_parameters=[specialization])
	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)


class VacancyView(generics.RetrieveAPIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]
	queryset = Vacancy.objects.all()
	serializer_class = FullVacancySerializer


def check_user_role(user: User, required_role: int):
	if user.role != required_role:
		raise exceptions.AuthenticationFailed("Неподходящая роль пользователя для этого действия")
	return True


class MyCVGetUpdateView(APIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]

	@swagger_auto_schema(responses={
		200: openapi.Response("Данные соискателя", FullApplicantSerializer),
		401: openapi.Response(
			description="Неподходящая роль пользователя для этого действия"
		)
	})
	def get(self, request, *args, **kwargs):
		check_user_role(request.user, ROLE_APPLICANT)
		user_cv = Applicant.objects.get(user=request.user)
		serializer = FullApplicantSerializer(user_cv)
		return Response(serializer.data)

	@swagger_auto_schema(responses={
		200: openapi.Response(
			description="Сообщение об успешной операции",
			examples={
				"application/json": {
					"message": "ok",
				}
			}),
		401: openapi.Response(
			description="Неподходящая роль пользователя для этого действия"
		)
	})
	def patch(self, request, *args, **kwargs):
		check_user_role(request.user, ROLE_APPLICANT)
		user_cv = Applicant.objects.get(user=request.user)
		serializer = EditApplicantSerializer(user_cv, data=request.data, partial=True)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response({"message": "ok"})


class CoursesForCVListView(generics.ListAPIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]
	serializer_class = CourseSerializer

	def get_queryset(self):
		check_user_role(self.request.user, ROLE_APPLICANT)
		user_cv = Applicant.objects.get(user=self.request.user)
		user_specs = \
			set([applicant_courses.course.spec.id for applicant_courses in user_cv.courses.all()] + \
			    [history.spec.id for history in user_cv.work_history.all() if history.spec])
		queryset = Course.objects.filter(required_spec__in=user_specs)
		if "specialization" in self.request.GET:
			queryset = queryset.filter(spec=self.request.GET["specialization"])
		return queryset

	@swagger_auto_schema(manual_parameters=[specialization], responses={
		401: openapi.Response(
			description="Неподходящая роль пользователя для этого действия"
		)
	})
	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)


class VacanciesForCVListView(APIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]

	@swagger_auto_schema(responses={
		200: openapi.Response("Данные вакансий", FullVacancySerializer(many=True)),
		401: openapi.Response(
			description="Неподходящая роль пользователя для этого действия"
		)
	})
	def get(self, request, *args, **kwargs):
		check_user_role(self.request.user, ROLE_APPLICANT)
		user_cv = Applicant.objects.get(user=self.request.user)
		user_specs = \
			set([applicant_courses.course.spec.id for applicant_courses in user_cv.courses.all()] + \
			    [history.spec.id for history in user_cv.work_history.all() if history.spec])
		user_education = user_cv.education.aggregate(Max("education_level"))["education_level__max"]

		vacancies = Vacancy.objects \
			.filter(closed_date=None) \
			.filter(specs__in=user_specs) \
			.filter(education_level__lte=user_education)

		serializer = FullVacancySerializer(vacancies, many=True)
		return Response(serializer.data)


class SpecializationsForCVListView(generics.ListAPIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]
	serializer_class = FullSpecializationSerializer

	def get_queryset(self):
		check_user_role(self.request.user, ROLE_APPLICANT)
		user_cv = Applicant.objects.get(user=self.request.user)
		user_specs = \
			set([applicant_courses.course.spec.id for applicant_courses in user_cv.courses.all()] + \
			    [history.spec.id for history in user_cv.work_history.all() if history.spec])
		queryset = Specialization.objects.filter(id__in=user_specs)
		return queryset

	@swagger_auto_schema(responses={
		401: openapi.Response(
			description="Неподходящая роль пользователя для этого действия"
		)
	})
	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)


class MyCompanyView(APIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]

	@swagger_auto_schema(responses={
		200: openapi.Response("Данные работодателя", FullCompanyAndVacanciesSerializer),
		401: openapi.Response(
			description="Неподходящая роль пользователя для этого действия"
		)
	})
	def get(self, request, *args, **kwargs):
		check_user_role(request.user, ROLE_HR)
		user_hr = HR.objects.get(user=request.user)
		company = user_hr.company.all()[0]
		serializer = FullCompanyAndVacanciesSerializer(company)
		return Response(serializer.data)


class GetListAndCreateVacancyListView(APIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]

	@swagger_auto_schema(responses={
		200: openapi.Response("Данные вакансий", ShortVacancyWithoutCompanySerializer(many=True)),
		401: openapi.Response(
			description="Неподходящая роль пользователя для этого действия"
		)
	})
	def get(self, request, *args, **kwargs):
		check_user_role(request.user, ROLE_HR)
		user_hr = HR.objects.get(user=request.user)
		company = user_hr.company.all()[0]
		serializer = ShortVacancyWithoutCompanySerializer(company.vacancies.all(), many=True)
		return Response(serializer.data)

	@swagger_auto_schema(responses={
		200: openapi.Response(
			description="Сообщение об успешной операции",
			examples={
				"application/json": {
					"message": "ok",
				}
			}),
		401: openapi.Response(
			description="Неподходящая роль пользователя для этого действия"
		)
	})
	def post(self, request, *args, **kwargs):
		check_user_role(request.user, ROLE_HR)
		user_hr = HR.objects.get(user=request.user)
		company = user_hr.company.all()[0]

		serializer = CreateVacancySerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save(company=company)
		return Response(serializer.data, status=201)


class GetAndUpdateVacancyView(APIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]

	@swagger_auto_schema(responses={
		200: openapi.Response("Данные вакансии", FullVacancySerializer),
		401: openapi.Response(
			description="Неподходящая роль пользователя для этого действия"
		)
	})
	def get(self, request, pk, *args, **kwargs):
		check_user_role(request.user, ROLE_HR)
		user_hr = HR.objects.get(user=request.user)
		company = user_hr.company.all()[0]
		vacancy = company.vacancies.get(id=pk)
		serializer = FullVacancySerializer(vacancy)
		return Response(serializer.data)

	@swagger_auto_schema(responses={
		200: openapi.Response(
			description="Сообщение об успешной операции",
			examples={
				"application/json": {
					"message": "ok",
				}
			}),
		401: openapi.Response(
			description="Неподходящая роль пользователя для этого действия"
		)
	})
	def patch(self, request, pk, *args, **kwargs):
		check_user_role(request.user, ROLE_HR)
		user_hr = HR.objects.get(user=request.user)
		company = user_hr.company.all()[0]
		vacancy = company.vacancies.get(id=pk)
		serializer = EditVacancySerializer(vacancy, data=request.data, partial=True)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response({"message": "ok"})


class GetCVSForVacancyListView(APIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]

	@swagger_auto_schema(responses={
		200: openapi.Response("Данные резюме", FullApplicantSerializer(many=True)),
		401: openapi.Response(
			description="Неподходящая роль пользователя для этого действия"
		)
	})
	def get(self, request, pk, *args, **kwargs):
		check_user_role(request.user, ROLE_HR)
		user_hr = HR.objects.get(user=request.user)
		company = user_hr.company.all()[0]
		vacancy = company.vacancies.get(id=pk)
		spec_ids = [spec.id for spec in vacancy.specs.all()]

		applicants = Applicant.objects \
			.filter(Q(work_history__spec__id__in=spec_ids) | Q(courses__course__spec__id__in=spec_ids)) \
			.filter(education__education_level__gte=vacancy.education_level)

		serializer = FullApplicantSerializer(applicants, many=True)
		return Response(serializer.data)


class CVSListView(generics.ListAPIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]
	serializer_class = ShortApplicantSerializer

	def get_queryset(self):
		check_user_role(self.request.user, ROLE_HR)
		queryset = Applicant.objects.all()
		if "specialization" in self.request.GET:
			spec = self.request.GET["specialization"]
			queryset = queryset.filter(Q(work_history__spec__id=spec) | Q(courses__course__spec__id=spec))
		return queryset

	@swagger_auto_schema(manual_parameters=[specialization], responses={
		401: openapi.Response(
			description="Неподходящая роль пользователя для этого действия"
		)
	})
	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)


class CVView(APIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]

	@swagger_auto_schema(responses={
		200: openapi.Response("Резюме пользователя", FullApplicantSerializer),
		401: openapi.Response(
			description="Неподходящая роль пользователя для этого действия"
		)
	})
	def get(self, request, pk):
		check_user_role(self.request.user, ROLE_HR)
		applicant = Applicant.objects.get(user=pk)
		serializer = FullApplicantSerializer(applicant)
		return Response(serializer.data)
