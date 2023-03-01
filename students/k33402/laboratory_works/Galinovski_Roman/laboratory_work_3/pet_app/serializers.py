from rest_framework import serializers
from django.db.models import Q
from .models import *


class OrganizerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organizer
        fields = "__all__"


class OwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Owner
        fields = "__all__"


class ClubSerializer(serializers.ModelSerializer):

    class Meta:
        model = Club
        fields = "__all__"


class DogSerializer(serializers.ModelSerializer):
    dog_owner = OwnerSerializer()
    dog_club = ClubSerializer()

    class Meta:
        model = Dog
        fields = ["id", "name", "breed", "full_age", "month_age","classof_dog", "document",
                  "last_vaccination", "owner", "club"]


class DogRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dog
        fields = ["name", "breed", "full_age", "month_age", "classof_dog", "document",
                  "last_vaccination", "owner", "club"]


class ShowSerializer(serializers.ModelSerializer):
    host = OrganizerSerializer

    class Meta:
        model = Show
        fields = "__all__"


class DogParticipationSerializer(serializers.ModelSerializer):
    participant_dog = DogSerializer()
    show_dog = ShowSerializer()

    class Meta:
        model = DogParticipation
        fields = ["id", "show_dog_number", "status", "dateof_reg_dog", "bill", "checkup", "dateof_checkup",
                  "participant_dog", "show_dog", "show_medal"]


class DogParticipationRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = DogParticipation
        fields = ["id", "show_dog_number", "status", "dateof_reg_dog", "bill", "checkup", "dateof_checkup",
                  "participant_dog", "show_dog", "show_medal"]


class ExpertSerializer(serializers.ModelSerializer):
    club = ClubSerializer

    class Meta:
        model = Expert
        fields = "__all__"


class ExpertParticipationSerializer(serializers.ModelSerializer):
    participant_exp = ExpertSerializer
    show_exp = ShowSerializer

    class Meta:
        model = ExpertParticipation
        fields = "__all__"


class SponsorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sponsor
        fields = "__all__"


class SponsorshipSerializer(serializers.ModelSerializer):
    sponsor = SponsorSerializer
    sponsor_show = ShowSerializer

    class Meta:
        model = Sponsorship
        fields = "__all__"


class ShowScheduleSerializer(serializers.ModelSerializer):
    show_schedule = ShowSerializer

    class Meta:
        model = ShowSchedule
        fields = "__all__"


class GradingSerializer(serializers.ModelSerializer):
    dog = DogParticipationSerializer
    expert = ExpertParticipationSerializer
    schedule = ShowScheduleSerializer

    class Meta:
        model = Grading
        fields = "__all__"


class DogRingSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer(many=True)
    dog = DogSerializer(many=True)
    show = ShowSerializer(many=True)
    dog_reg = DogParticipationSerializer(many=True)

    class Meta:
        model = ShowSchedule
        fields = ["__all__"]


class DogBreedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dog
        fields = ["breed"]


class ClubBreedSerializer(serializers.ModelSerializer):
    members = DogBreedSerializer(many=True)

    class Meta:
        model = Club
        fields = ["name", "members"]


class DogNotAllowedOrSuspendedCountSerializer(serializers.ModelSerializer):
    miss_count = serializers.SerializerMethodField()

    class Meta:
        model = Show
        fields = ["dateof_begin", "miss_count"]

    def get_count(self, obj):
        return obj.show_dog_reg.filter(Q(status="Suspended") | Q(status="Not allowed")).count()


class BreedExpertsSerializer(serializers.ModelSerializer):
    show_schedule = ShowScheduleSerializer(many=True)
    experts_reg = ExpertParticipationSerializer(many=True)
    experts = ExpertSerializer(many=True)

    class Meta:
        model = Grading
        fields = ["__all__"]