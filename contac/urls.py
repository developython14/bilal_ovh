from django.urls import path, include
from rest_framework import permissions ,routers
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
router.register(r'contacts', contactview)

urlpatterns = [
    path('', include(router.urls)),
    ]