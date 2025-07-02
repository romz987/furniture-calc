from django.urls import path 
from users.apps import UsersConfig  
from users.views import *

app_name = UsersConfig.name 


urlpatterns = [
    path('register/', user_register_view, name='user_register'),
    path('login/', user_login_view, name='user_login'),
    path('registration-success/', successful_register_view, name='user_registered'),
    path('password-recovery/', restore_password_view, name='password_recovery'),
    path('logout/', user_logout_view, name='user_logout'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
]
