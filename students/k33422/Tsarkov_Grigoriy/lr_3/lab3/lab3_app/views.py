from rest_framework import generics
from rest_framework.views import APIView, Response
from .serializers import *
from .models import *
from django.db.models.aggregates import Count, Sum


class ExpertAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExpertSerializer
    queryset = Expert.objects.all()


class ParticipationAPIList(generics.ListCreateAPIView):
    serializer_class = ParticipationSerializer
    queryset = Participation.objects.all()


class ParticipantAPIList(generics.ListCreateAPIView):
    serializer_class = ParticipantSerializer
    queryset = Participant.objects.all()


class StageParticipationAPIView(generics.RetrieveAPIView):
    serializer_class = StageParticipationSerializer
    queryset = Participation.objects.all()


class ClubFandomsRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ClubFandomsSerializer
    queryset = Club.objects.all()


class DismissedCountAPIView(generics.RetrieveAPIView):
    serializer_class = DismissedCountSerializer
    queryset = Participation.objects.all()


class FandomExpertsAPIView(generics.ListAPIView):
    serializer_class = FandomExpertsSerializer
    queryset = Stage.objects.all()


class FandomCountAPIView(APIView):

    def get(self, request):
        fandom_count = Participant.objects \
            .values('fandom').annotate(count=Count('fandom'))
        content = {'fandom_count': fandom_count}
        return Response(content)


class FandomCountAPIView(APIView):

    def get(self, request):
        fandom_count = Stage.objects \
            .values('fandom').annotate(count=Count('fandom'))
        content = {'fandom_count': fandom_count}
        return Response(content)


class ReportAPIView(APIView):

    def get(self, request, year):
        participants = Show.objects.get(year=year).participants
        participant_count = participants.count()
        fandom_count = participants.values('fandom').annotate(count=Count('fandom'))
        best_grades = Participation.objects.filter(stage__show__year=year)\
            .values('participant')\
            .annotate(ex_sum=Sum('final_grade'))\
            .order_by()
        medals = Participation.objects.values('stage__fandom')\
            .annotate(medals_count=Count('medal'))
        content = {'participant_count': participant_count,
                   'fandoms': fandom_count,
                   'best_grades': best_grades,
                   'medals': medals}
        return Response(content)
