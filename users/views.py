import random
import string
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.edit import FormView
# Формы
from users.forms import (
    UserLoginForm,
    UserRegisterForm,
    UserUpdateForm,
    MySetPasswordForm,
)
# Воостановление пароля
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetConfirmView
)
# Мои сервисы и модели
from django.views.generic import UpdateView, CreateView
from users.models import User, ActiveInvites
from users.services import (
    send_register_verification_email,
    send_register_success_email,
)

# Генерация токена для подтверждения регистрации
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.encoding import force_str


# Логин
class UserLoginView(FormView):
    template_name = 'users/user_login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('furniture:index')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        user = authenticate(
            email=cleaned_data['email'],
            password=cleaned_data['password']
        )
        if user is not None and user.is_active:
            login(self.request, user)
            return super().form_valid(form)
        form.add_error(None, 'Неверный email или пароль.')
        return self.form_invalid(form)


# Регистрация
class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/user_register.html'
    success_url = reverse_lazy('users:user-registered')

    def dispatch(self, request, *args, **kwargs):
        # Проверка на авториазацию
        if request.user.is_authenticated:
            return redirect('furniture:index')
        # Проверка на инвайт
        self.invite_number = request.GET.get('invite')
        self.invite_code = get_object_or_404(
            ActiveInvites, invite_number=self.invite_number)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.invite_number = self.invite_code
        user.is_active = False
        user.save()
        # Удаляем инвайт
        self.invite_code.delete()
        # Подтверждения регистрации
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        # Собираем ссылку
        activation_link = self.request.build_absolute_uri(
            reverse(
                "users:activate-account",
                kwargs={"uidb64": uid, "token": token}
            )
        )
        send_register_verification_email(user.email, activation_link)
        return HttpResponseRedirect(reverse('users:user-registered'))

    def form_invalid(self, form):
        messages.error(
            self.request,
            'Проверьте правильность введённых данных.'
        )
        return super().form_invalid(form)


# Подтверждение аккаунта
def activate_account_view(request, uidb64, token):
    try:
        # Декодируем uid из base64 обратно в строку, затем в int
        uid = force_str(urlsafe_base64_decode(uidb64))
        # Получаем объект пользователя по uid
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        send_register_success_email(user.email)
        return redirect('users:activation-success')
    else:
        return redirect('users:activation-failed')


# Успешная регистрация
def successful_register_view(request):
    template_name = 'users/user_registration_success.html'
    return render(request, template_name)


# Неуспешная активация аккаунта
def activation_failed_view(request):
    template_name = 'users/user_activation_failed.html'
    return render(request, template_name)


# Успешная активация аккаунта
def activation_success_view(request):
    template_name = 'users/user_activation_success.html'
    return render(request, template_name)


# Запрос на восстановление пароля
class MyPasswordResetView(PasswordResetView):
    template_name = 'users/user_password_recovery.html'
    email_template_name = 'email/password_reset_email.html'
    success_url = reverse_lazy('users:user-login')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)


# Форма восстановление пароля
class MyPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'users/user_password_recovery_form.html'
    form_class = MySetPasswordForm
    success_url = reverse_lazy('users:password-reset-success')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)


# Успешная смена пароля
def password_changed_view(request):
    if request.user.is_authenticated:
        return redirect('furniture:index')
    template_name = 'users/user_password_recovery_success.html'
    return render(request, template_name)


# Выход из аккаунта
@login_required
def user_logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:user-login'))


# Управление профилем пользователя
class UserProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'users/user_profile.html'
    success_url = reverse_lazy('furniture:index')

    def get_object(self, queryset=None):
        return self.request.user


# Админ: управление пользователями
@login_required
def manage_users_view(request):
    # Проверка привилегий
    if not request.user.is_superuser:
        raise Http404
    # Возврашаем страницу
    template_name = 'admin/admin_manage_users.html'
    objects_list = User.objects.filter(is_superuser=False)
    invites_list = ActiveInvites.objects.all()
    context = {
        'title': 'Управление пользователями',
        'objects_list': objects_list,
        'invites_list': invites_list,
    }
    return render(request, template_name, context=context)


# Админ: переключение активности пользователя
@login_required
def toggle_user_active_view(request, pk):
    # Проверка привилегий
    if not request.user.is_superuser:
        raise Http404
    # Меняем активность
    user = get_object_or_404(User, pk=pk)
    user.is_active = not user.is_active
    user.save()
    return redirect('users:manage-users')


# Админ: создание инвайта
class GenerateInviteView(LoginRequiredMixin, View):
    template_name = 'admin/admin_generate_invite.html'
    model = ActiveInvites

    def get(self, request):
        # Проверка привилегий
        if not request.user.is_superuser:
            raise Http404
        return render(request, self.template_name)

    def post(self, request):
        # Проверка привилегий
        if not request.user.is_superuser:
            raise Http404
        # Генерируем значение инвайта
        invite_number = self.__gen_invite_number()
        # Создаем ссылку
        registration_url = (
            request.scheme +
                '://' + request.get_host() +
                    '/user/register/?invite=' +
                        invite_number
        )
        # Сохраняем значение в базу данных
        record_object = self.model(
            invite_number=invite_number,
            invite_url=registration_url
        )
        record_object.save()
        # Отдаем ссылку в шаблон
        context = {
            'reg_url': registration_url,
        }
        return render(request, self.template_name, context=context)

    def __gen_invite_number(self):
        # Дата и время
        timestamp_part = datetime.now().strftime('%d%m%y%H%M')
        # 20 случайных цифр
        alphabet = string.ascii_letters + string.digits
        random_part = ''.join(random.choices(alphabet, k=30))
        return timestamp_part + random_part


# Детальная информация об инвайте
@login_required
def invite_details_view(request, pk):
    # Проверка привилегий
    if not request.user.is_superuser:
        raise Http404
    invite_record = get_object_or_404(ActiveInvites, pk=pk)
    template_name = 'admin/admin_invite_details.html'
    context = {
        'invite': invite_record,
    }
    return render(request, template_name, context=context)


# Удаление инвайта
@login_required
def delete_invite_view(request, pk):
    # Проверка привилегий
    if not request.user.is_superuser:
        raise Http404
    invite_record = get_object_or_404(ActiveInvites, pk=pk)
    invite_record.delete()
    return redirect('users:manage-users')
