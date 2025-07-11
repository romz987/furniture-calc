from django.urls import path
from users.apps import UsersConfig
from users.views import (
    user_register_view,
    user_login_view,
    successful_register_view,
    restore_password_view,
    user_logout_view,
    manage_users_view,
    toggle_user_active_view,
    invite_details_view,
    delete_invite_view,
    activate_account_view,
    UserProfileView,
    GenerateInviteView,
    UserRegisterView,
)

app_name = UsersConfig.name


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('login/', user_login_view, name='user-login'),
    path('registration-success/', successful_register_view, name='user-registered'),
    path('password-recovery/', restore_password_view, name='password-recovery'),
    path('logout/', user_logout_view, name='user-logout'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    # admin
    path('management/manage-users/', manage_users_view, name='manage-users'),
    path('management/togggle-user-activity/<int:pk>/', toggle_user_active_view, name="toggle-user-activity"),
    path('management/generate-invite/', GenerateInviteView.as_view(), name="generate-invite"),
    path('management/invite-details/<int:pk>/', invite_details_view, name="invite-details"),
    path('management/delete_invite/<int:pk>/', delete_invite_view, name="delete-invite"),
    # activate account
    path('activate/<uidb64>/<token>/', activate_account_view, name='activate-account'),
]
