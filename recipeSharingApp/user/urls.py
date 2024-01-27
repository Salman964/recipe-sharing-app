# user/urls.py
from django.urls import path
from .views import user_profile, follow_user

app_name = 'user'

urlpatterns = [
    path('<str:username>/', user_profile, name='user_profile'),
    path('<str:username>/follow/', follow_user, name='follow_user'),
]
