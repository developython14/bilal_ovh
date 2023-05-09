from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
#url patterfn about levels
urlpatterns =[
    path('student_login/',student_login, name="student_login"),
    path('create_account/',create_account, name="create_account"),
    path('put_account/',put_account, name="put_account"),
    path('remove_account/',remove_account, name="remove_account"),
]
