from rest_framework import serializers
from .models import rstudent

class rstudentserializer(serializers.ModelSerializer):
    class Meta:
        model = rstudent
        fields = '__all__'