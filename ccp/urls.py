from django.urls import path, include
from rest_framework import permissions ,routers
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
router.register(r'ccp', ccpview)
router.register(r'ccp_images', ccpimageview)

urlpatterns = [
    path('', include(router.urls)),]