from django.urls import path 
from users.apps import UsersConfig  
from users.views import (
    user_register_view,
    user_login_view,
    successful_register_view,
    restore_password_view,
    user_logout_view,
    UserProfileView,
    manage_users_view,
    toggle_user_active_view,
)

app_name = UsersConfig.name 


urlpatterns = [
    path('register/', user_register_view, name='user_register'),
    path('login/', user_login_view, name='user_login'),
    path('registration-success/', successful_register_view, name='user_registered'),
    path('password-recovery/', restore_password_view, name='password_recovery'),
    path('logout/', user_logout_view, name='user_logout'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    # admin
    path('management/manage-users/', manage_users_view, name='manage_users'),
    path('management/togggle-user-activity/<int:pk>/', toggle_user_active_view, name="toggle_user_activity")
]
