from django.urls import path
from .views import *

urlpatterns = [
    path('comments/', comments, name='comments-drf'),
    path('', user_profile, name='user-profile-drf'),
    path('<int:pk>/', update_delete_user_profile, name='update_delete_user-profile-drf'),
    path('users/', UserProfileView.as_view(), name='user-profile-class-base-view-get-post'),
    path('users/<pk>/', UserProfileView.as_view(), name='user-profile-class-base-view-update-and-delete'),
]
