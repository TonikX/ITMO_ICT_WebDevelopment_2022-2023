from rest_framework import serializers

from lab_application.models import *


class FullSpecializationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Specialization
		fields = "__all__"


class ShortSpecializationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Specialization
		fields = ["id", "name", "level_name"]

	def to_representation(self, instance):
		response = super().to_representation(instance)
		response = {
			"id": response["id"],
			"name": response["name"] + f"({response['level_name']})" if response['level_name'] else ""
		}
		return response


class ShortCompanySerializer(serializers.ModelSerializer):
	class Meta:
		model = Company
		fields = ["id", "name"]


class ShortVacancySerializer(serializers.ModelSerializer):
	company = ShortCompanySerializer(read_only=True)
	specs = ShortSpecializationSerializer(many=True, read_only=True)

	class Meta:
		model = Vacancy
		fields = ["id", "company", "specs", "salary", "created_date"]


class FullUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ["id", "first_name", "last_name", "phone", "email"]


class FullHRSerializer(serializers.ModelSerializer):
	user = FullUserSerializer(read_only=True)

	class Meta:
		model = HR
		fields = "__all__"


class FullCompanySerializer(serializers.ModelSerializer):
	hr = FullHRSerializer(read_only=True)

	class Meta:
		model = Company
		fields = "__all__"


class ShortVacancyWithoutCompanySerializer(serializers.ModelSerializer):
	specs = ShortSpecializationSerializer(many=True, read_only=True)

	class Meta:
		model = Vacancy
		fields = ["id", "specs", "salary", "created_date", "closed_date"]


class FullCompanyAndVacanciesSerializer(serializers.ModelSerializer):
	hr = FullHRSerializer(read_only=True)
	vacancies = ShortVacancyWithoutCompanySerializer(many=True, read_only=True)

	class Meta:
		model = Company
		fields = ["id", "name", "address", "hr", "vacancies"]


class FullVacancySerializer(serializers.ModelSerializer):
	company = FullCompanySerializer(read_only=True)
	education_level = serializers.CharField(source="get_education_level_display", read_only=True)
	specs = FullSpecializationSerializer(many=True, read_only=True)

	class Meta:
		model = Vacancy
		fields = "__all__"


class FullApplicantHistorySerializer(serializers.ModelSerializer):
	spec = FullSpecializationSerializer(read_only=True)

	class Meta:
		model = ApplicantHistory
		fields = ["spec", "salary", "start_date", "end_date"]


class FullApplicantEducationSerializer(serializers.ModelSerializer):
	education_level = serializers.CharField(source="get_education_level_display", read_only=True)

	class Meta:
		model = ApplicantEducation
		fields = ["education_level", "description", "start_date", "end_date"]


class CourseSerializer(serializers.ModelSerializer):
	spec = ShortSpecializationSerializer(read_only=True)
	required_spec = ShortSpecializationSerializer(read_only=True)

	class Meta:
		model = Course
		fields = ["id", "name", "description", "spec", "required_spec"]


class ApplicantCoursesSerializer(serializers.ModelSerializer):
	course = CourseSerializer(read_only=True)

	class Meta:
		model = ApplicantCourses
		fields = ["course", "start_date", "end_date"]


class ShortUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ["id", "first_name", "last_name"]


class ShortApplicantSerializer(serializers.ModelSerializer):
	user = ShortUserSerializer(read_only=True)
	specializations = serializers.SerializerMethodField("get_specializations")

	class Meta:
		model = Applicant
		fields = ["user", "specializations"]

	def get_specializations(self, applicant: Applicant):
		user_specs = \
			set([applicant_courses.course.spec.id for applicant_courses in applicant.courses.all()] + \
			    [history.spec.id for history in applicant.work_history.all() if history.spec])
		specs = Specialization.objects.filter(id__in=user_specs)
		return FullSpecializationSerializer(specs, many=True).data

	def to_representation(self, instance):
		response = super().to_representation(instance)
		response["id"] = response["user"]["id"]
		return response


class FullApplicantSerializer(serializers.ModelSerializer):
	user = FullUserSerializer(read_only=True)
	work_history = FullApplicantHistorySerializer(many=True, read_only=True)
	education = FullApplicantEducationSerializer(many=True, read_only=True)
	courses = ApplicantCoursesSerializer(many=True, read_only=True)

	class Meta:
		model = Applicant
		fields = ["user", "work_history", "education", "courses"]

	def to_representation(self, instance):
		response = super().to_representation(instance)
		response["id"] = response["user"]["id"]
		return response


class EditSpecializationSerializer(serializers.ModelSerializer):
	id = serializers.IntegerField()

	class Meta:
		model = Specialization
		fields = ["id"]


class EditApplicantHistorySerializer(serializers.ModelSerializer):
	spec = EditSpecializationSerializer()

	class Meta:
		model = ApplicantHistory
		fields = ["spec", "salary", "start_date", "end_date"]


class EditApplicantEducationSerializer(serializers.ModelSerializer):
	education_level = serializers.IntegerField()

	class Meta:
		model = ApplicantEducation
		fields = ["education_level", "description", "start_date", "end_date"]


class EditApplicantSerializer(serializers.ModelSerializer):
	work_history = EditApplicantHistorySerializer(many=True)
	education = EditApplicantEducationSerializer(many=True)

	class Meta:
		model = Applicant
		fields = ["work_history", "education"]

	def update(self, instance: Applicant, validated_data):
		if "work_history" in validated_data:
			whs = validated_data.pop("work_history")
			instance.work_history.all().delete()
			for wh in whs:
				if wh["spec"]:
					wh["spec"] = Specialization.objects.get(id=wh["spec"]["id"])
				instance.work_history.add(
					ApplicantHistory.objects.create(applicant=instance, **wh)
				)

		if "education" in validated_data:
			edus = validated_data.pop("education")
			instance.education.all().delete()
			for edu in edus:
				instance.education.add(
					ApplicantEducation.objects.create(applicant=instance, **edu)
				)

		instance.save()
		return instance


class CreateVacancySerializer(serializers.ModelSerializer):
	specs = EditSpecializationSerializer(many=True)
	company = ShortCompanySerializer(read_only=True)

	class Meta:
		model = Vacancy
		fields = ["company", "education_level", "seniority", "salary", "description", "specs"]

	def create(self, validated_data):
		specs = [
			Specialization.objects.get(id=spec["id"])
			for spec in validated_data.pop("specs")
		]
		vacancy = Vacancy.objects.create(**validated_data)
		vacancy.specs.add(*specs)
		return vacancy


class EditVacancySerializer(serializers.ModelSerializer):
	specs = EditSpecializationSerializer(many=True)

	class Meta:
		model = Vacancy
		fields = ["education_level", "seniority", "salary", "description", "specs", "closed_date"]

	def update(self, instance: Vacancy, validated_data):
		if "specs" in validated_data:
			specs = [
				Specialization.objects.get(id=spec["id"])
				for spec in validated_data.pop("specs")
			]

			instance.specs.clear()
			instance.specs.add(*specs)

		for key, value in validated_data.items():
			instance.__setattr__(key, value)
		instance.save()
		return instance
