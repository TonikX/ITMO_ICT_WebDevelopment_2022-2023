from rest_framework import serializers
from .models import *

'''Организатору выставки могут потребоваться следующие сведения;
 На каком ринге выступает заданный хозяин со своей собакой? !
 Какими породами представлен заданный клуб? !
 Сколько собак были отстранены от участия в выставке? !
 Какие эксперты обслуживают породу? !
 Количество участников по каждой породе?'''



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
    '''На каком ринге выступает заданный хозяин со своей собакой?'''

    class Meta:
        model = Participation
        fields = ["rings"]


class ParticipantBreedsSerializer(serializers.ModelSerializer):
    '''Количество участников по каждой породе?'''
    class Meta:
        model = Participant
        fields = ["breed"]


class ClubBreedsSerializer(serializers.ModelSerializer):
    '''Какими породами представлен заданный клуб?'''
    members = ParticipantBreedsSerializer(many=True)

    class Meta:
        model = Club
        fields = ["name", "members"]


class RingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ring
        fields = "__all__"


class DismissedCountSerializer(serializers.ModelSerializer):
    '''Сколько собак были отстранены от участия в выставке?'''
    dismissed_count = serializers.SerializerMethodField()

    class Meta:
        model = Participation
        fields = ['dismissed_count']

    def get_dismissed_count(self, obj):
        return Participation.objects.filter(dismissed=True).count()


class BreedExpertsSerializer(serializers.ModelSerializer):
    '''Какие эксперты обслуживают породу?'''
    experts = ExpertSerializer(many=True)

    class Meta:
        model = Ring
        fields = ["breed", "experts"]

