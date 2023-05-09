from rest_framework import viewsets ,status
from rest_framework import permissions 
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializer import *
from django.http import Http404
from .models import *


from .serializer import *
from django.urls import path, include



class ccpview(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = ccp.objects.all()
    serializer_class = ccpSerializer
    permission_classes = [permissions.AllowAny]



class ccpimageview(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = ccp_image.objects.all()
    serializer_class = ccpimageSerializer
    permission_classes = [permissions.AllowAny]

