from rest_framework import serializers
from .models import YogaParticipant

class YogaParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = YogaParticipant
        fields = '__all__'