from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    email =  serializers.CharField(max_length=200)

    class Meta:
        model = Person
        fields = ('__all__')