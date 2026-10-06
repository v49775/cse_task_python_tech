from rest_framework import serializers
from .models import jobs


class job_serializer(serializers.ModelSerializer):
    class Meta:
        model = jobs
        fields = '__all__'