from .models import *
from rest_framework import serializers


class ccpSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = ccp
        fields = ['id','created','title']


class ccpimageSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = ccp_image
        fields = ['id','created','page_de_garde']
