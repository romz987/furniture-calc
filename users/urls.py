from django.urls import path
from users.apps import UsersConfig
from users.views import (
    # Авторизация и регистрация
    UserLoginView,
    UserRegisterView,
    # Подтверждение аккаунта
    activation_failed_view,
    activation_success_view,
    # Остальное
    successful_register_view,
    user_logout_view,
    manage_users_view,
    toggle_user_active_view,
    invite_details_view,
    delete_invite_view,
    activate_account_view,
    # Управление пользователями
    UserProfileView,
    GenerateInviteView,
    # Сброс пароля
    MyPasswordResetView,
    MyPasswordResetConfirmView,
    password_changed_view,
)

app_name = UsersConfig.name


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('registration-success/', successful_register_view, name='user-registered'),
    # path('password-recovery/', restore_password_view, name='password-recovery'),
    path('logout/', user_logout_view, name='user-logout'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    # admin
    path('management/manage-users/', manage_users_view, name='manage-users'),
    path('management/toggle-user-activity/<int:pk>/', toggle_user_active_view, name="toggle-user-activity"),
    path('management/generate-invite/', GenerateInviteView.as_view(), name="generate-invite"),
    path('management/invite-details/<int:pk>/', invite_details_view, name="invite-details"),
    path('management/delete-invite/<int:pk>/', delete_invite_view, name="delete-invite"),
    # activate account
    path('activate/<uidb64>/<token>/', activate_account_view, name='activate-account'),
    path('activation-failed/', activation_failed_view, name='activation-failed'),
    path('activation-success/', activation_success_view, name='activation-success'),
    # reset password
    path('password-reset/', MyPasswordResetView.as_view(), name='password-recovery'),
    path('password-set-new/<uidb64>/<token>/', MyPasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    path('password-reset-success/', password_changed_view, name='password-reset-success'),
]
