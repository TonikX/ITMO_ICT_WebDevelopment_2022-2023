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


class RingParticipationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Participation
        fields = ["rings"]


class ParticipantBreedsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Participant
        fields = ["breed"]


class ClubBreedsSerializer(serializers.ModelSerializer):
    members = ParticipantBreedsSerializer(many=True)

    class Meta:
        model = Club
        fields = ["name", "members"]


class RingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ring
        fields = "__all__"


class DismissedCountSerializer(serializers.ModelSerializer):

    dismissed_count = serializers.SerializerMethodField()

    class Meta:
        model = Participation
        fields = ["dismissed_count"]

    def get_dismissed_count(self, obj):
        return Participation.objects.filter(dismissed=True).count()


class BreedExpertsSerializer(serializers.ModelSerializer):
    experts = ExpertSerializer(many=True)

    class Meta:
        model = Ring
        fields = ["breed", "experts"]

