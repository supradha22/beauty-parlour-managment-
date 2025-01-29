from rest_framework import serializers
from.models import*
class work(serializers.Serializer):
    name1=serializers.CharField(max_length=20)
    branch=serializers.CharField(max_length=50)