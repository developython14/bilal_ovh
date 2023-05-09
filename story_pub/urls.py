from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
#url patterfn about levels
urlpatterns =[
    path('get_stories/',get_stories, name="get_stories"),
    path('post_stories/',post_stories, name="post_stories"),
    path('remove_stories/',remove_stories, name="remove_stories"),
    path('put_stories/',put_stories, name="put_stories"),
    path('remove_stories_files/',remove_stories_files, name="remove_stories_files"),
]



urlpatterns +=[
    path('get_pubs/',get_pubs, name="get_pubs"),
    path('post_pubs/',post_pubs, name="post_pubs"),
    path('put_pubs/',put_pubs, name="put_pubs"),
    path('remove_pubs/',remove_pubs, name="remove_pubs"),
]
