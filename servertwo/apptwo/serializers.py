from .models import Sample
from rest_framework import serializers

class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sample
        fields = ('processed', 'message')
    