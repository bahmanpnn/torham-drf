from django.urls import path
from .views import *

urlpatterns = [
    path('', user_profile, name='user-profile-drf'),
    path('comments/', comments, name='comments-drf'),
]
