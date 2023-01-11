from rest_framework import serializers
from .models import *


class ExpertSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expert
        fields = "__all__"


class ParticipationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Participation
        fields = "__all__"


class ParticipantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Participant
        fields = "__all__"


class StageParticipationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Participation
        fields = ["stage"]


class ParticipantFandomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ["fandom"]


class ClubFandomsSerializer(serializers.ModelSerializer):
    members = ParticipantFandomsSerializer(many=True)

    class Meta:
        model = Club
        fields = ["name", "members"]


class StageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stage
        fields = "__all__"


class DismissedCountSerializer(serializers.ModelSerializer):
    dismissed_count = serializers.SerializerMethodField()

    class Meta:
        model = Participation
        fields = ['dismissed_count']

    def get_dismissed_count(self, obj):
        return Participation.objects.filter(dismissed=True).count()


class FandomExpertsSerializer(serializers.ModelSerializer):
    experts = ExpertSerializer(many=True)

    class Meta:
        model = Stage
        fields = ["fandom", "experts"]
