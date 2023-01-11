from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView, Response
from .serializers import *
from .models import *
from django.db.models.aggregates import *


class OwnerListAPIView(generics.ListAPIView):
    serializer_class = OwnerSerializer
    queryset = Owner.objects.all()


class OwnerAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OwnerSerializer
    queryset = Owner.objects.all()


class OwnerCreateAPIView(generics.CreateAPIView):
    serializer_class = OwnerSerializer
    queryset = Owner.objects.all()


class ClubListAPIView(generics.ListAPIView):
    serializer_class = ClubSerializer
    queryset = Club.objects.all()


class ClubAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClubSerializer
    queryset = Club.objects.all()


class ClubCreateAPIView(generics.CreateAPIView):
    serializer_class = ClubSerializer
    queryset = Club.objects.all()


class DogListAPIView(generics.ListAPIView):
    serializer_class = DogSerializer
    queryset = Dog.objects.all()


class DogAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DogRetrieveSerializer
    queryset = Dog.objects.all()


class DogCreateAPIView(generics.CreateAPIView):
    serializer_class = DogRetrieveSerializer
    queryset = Dog.objects.all()


class ShowListAPIView(generics.ListAPIView):
    serializer_class = ShowSerializer
    queryset = Show.objects.all()


class ShowAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ShowSerializer
    queryset = Show.objects.all()


class ShowCreateAPIView(generics.CreateAPIView):
    serializer_class = ShowSerializer
    queryset = Show.objects.all()


class DogParticipationListAPIView(generics.ListAPIView):
    serializer_class = DogParticipationSerializer
    queryset = DogParticipation.objects.all()


class DogParticipationAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DogParticipationRetrieveSerializer
    queryset = DogParticipation.objects.all()


class DogParticipantCreateAPIView(generics.CreateAPIView):
    serializer_class = DogParticipationRetrieveSerializer
    queryset = DogParticipation.objects.all()


class ExpertListAPIView(generics.ListAPIView):
    serializer_class = ExpertSerializer
    queryset = Expert.objects.all()


class ExpertAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExpertSerializer
    queryset = Expert.objects.all()


class ExpertCreateAPIView(generics.CreateAPIView):
    serializer_class = ExpertSerializer
    queryset = Expert.objects.all()


class ExpertParticipationListAPIView(generics.ListAPIView):
    serializer_class = ExpertParticipationSerializer
    queryset = ExpertParticipation.objects.all()


class ExpertParticipationAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExpertParticipationSerializer
    queryset = ExpertParticipation.objects.all()


class ExpertParticipationCreateAPIView(generics.CreateAPIView):
    serializer_class = ExpertParticipationSerializer
    queryset = ExpertParticipation.objects.all()


class SponsorListAPIView(generics.ListAPIView):
    serializer_class = SponsorSerializer
    queryset = Sponsor.objects.all()


class SponsorAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SponsorSerializer
    queryset = Sponsor.objects.all()


class SponsorCreateAPIView(generics.CreateAPIView):
    serializer_class = SponsorSerializer
    queryset = Sponsor.objects.all()


class SponsorshipListAPIView(generics.ListAPIView):
    serializer_class = SponsorshipSerializer
    queryset = Sponsorship.objects.all()


class SponsorshipAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SponsorshipSerializer
    queryset = Sponsorship.objects.all()


class SponsorshipCreateAPIView(generics.CreateAPIView):
    serializer_class = SponsorshipSerializer
    queryset = Sponsorship.objects.all()


class ShowScheduleListAPIView(generics.ListAPIView):
    serializer_class = ShowScheduleSerializer
    queryset = ShowSchedule.objects.all()


class ShowScheduleAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ShowScheduleSerializer
    queryset = ShowSchedule.objects.all()


class ShowScheduleCreateAPIView(generics.CreateAPIView):
    serializer_class = ShowScheduleSerializer
    queryset = ShowSchedule.objects.all()


class GradingListAPIView(generics.ListAPIView):
    serializer_class = GradingSerializer
    queryset = Grading.objects.all()


class GradingAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GradingSerializer
    queryset = Grading.objects.all()


class GradingCreateAPIView(generics.CreateAPIView):
    serializer_class = GradingSerializer
    queryset = Grading.objects.filter(~Q(dog_grade__dog_status="Не допущен/Not allowed"))


#class DogRingAPIView(generics.RetrieveAPIView):
#    serializer_class = DogRingSerializer
#    queryset = ShowSchedule.objects.all()


class DogRingAPIView(APIView):
    def get(self, request, id):
        rings = Grading.objects.filter(dog_grade__participant_dog__dog_owner__id=id).values(
            "schedule_grade__show_schedule__name", "schedule_grade__show_schedule__begin_date",
            "dog_grade__participant_dog__dog_name", "dog_grade__participant_dog__breed", "schedule_grade__ring_number")
        content = {"rings": rings}
        return Response(content)

#class ClubBreedAPIView(generics.RetrieveAPIView):
    #serializer_class = ClubBreedSerializer
    #queryset = Club.objects.all()


class ClubBreedAPIView(APIView):
    def get(self, request, id):
        breeds = Dog.objects.filter(dog_club__id=id).values("breed").annotate(count=Count("breed"))
        content = {"breeds": breeds}
        return Response(content)



#class DogNotAllowedOrSuspendedCountAPIView(generics.RetrieveAPIView):
    #serializer_class = DogNotAllowedOrSuspendedCountSerializer
    #queryset = Show.objects.all()
    #def get(self, request, show, year):


class DogNotAllowedOrSuspendedCountAPIView(APIView):
    def get(self, request, id):
        participants = DogParticipation.objects.filter(show_dog__id=id).filter(Q(dog_status="Не допущен/Not allowed") | Q(dog_status="Снят/Suspended"))
        counter = participants.count()
        dogs = participants.values("show_dog__name", "show_dog__begin_date", "participant_dog__breed", "participant_dog__dog_name")
        content = {"counter": counter, "dogs": dogs}
        return Response(content)




class BreedExpertsAPIView(APIView):
    #serializer_class = BreedExpertsSerializer
    #queryset = Grading.objects.all()
    def get(self, request):
        breeds = Grading.objects.values("dog_grade__participant_dog__breed", "expert_grade__participant_exp__expert_surname",
                                        "expert_grade__participant_exp__expert_name", "expert_grade__participant_exp__expert_patronymic").distinct().order_by("dog_grade__participant_dog__breed")
        content = {"breeds": breeds}
        return Response(content)


class BreedCountAPIView(APIView):
    def get(self, request):
        breed_counter = Dog.objects.values("breed").annotate(count=Count("breed"))
        content = {"breed_counter": breed_counter}
        return Response(content)


class ReportAPIView(APIView):
    def get(self, request, id):
        show = Show.objects.get(id=id)
        show_title = show.name
        year = show.begin_date.year
        participants = DogParticipation.objects.filter(show_dog__id=id)
        counter = participants.count()
        breed_counter = participants.values("participant_dog__breed").annotate(count=Count("participant_dog__breed"))
        best_grades = Grading.objects.filter(schedule_grade__show_schedule__id=id).values(
                                             "dog_grade__participant_dog__dog_name", "dog_grade__participant_dog__breed",
                                             "dog_grade__id", "grade1", "grade2", "grade3", "sum").order_by("dog_grade__participant_dog__breed", "sum")
        medals = DogParticipation.objects.filter(show_dog__id=id).values(
                                             "participant_dog__dog_name", "participant_dog__breed",
                                             "show_medal").annotate(medals_count=Count("show_medal")).order_by(
                                             "participant_dog__breed", "dog_grade__sum")
        content = {
            "show_title": show_title,
            "year": year,
            "participants_number": counter,
            "breeds": breed_counter,
            "best_grades": best_grades,
            "medals": medals
        }
        return Response(content)





