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
from django.views.generic import UpdateView
from users.forms import UserRegisterForm, UserLoginForm, UserUpdateForm
from users.models import User, ActiveInvites


def user_register_view(request):
    form = UserRegisterForm()
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:user_registered'))
        else:
            messages.error(request, 'Проверьте правильность введённых данных.')
    context = {
        'form': form
    }
    return render(request, 'users/user_register.html', context=context)


def user_login_view(request):
    form = UserLoginForm()
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = authenticate(
                email=cleaned_data['email'],
                password=cleaned_data['password']
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('furniture:index'))
            else:
                form.add_error(None, 'Неверный email или пароль.')
    context = {
        'form': form
    }
    return render(request, 'users/login_page.html', context=context)


def successful_register_view(request):
    return render(request, 'users/registration_success.html')


@login_required
def restore_password_view(request):
    return render(request, 'users/password_recovery.html')


@login_required
def user_logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:user_login'))


class UserProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'users/user_profile.html'
    success_url = reverse_lazy('furniture:index')

    def get_object(self, queryset=None):
        return self.request.user


# Админ
@login_required
def manage_users_view(request):
    # Проверка привилегий
    if not request.user.is_superuser:
        raise Http404
    # Возврашаем страницу
    template_name = 'admin/manage_users.html'
    objects_list = User.objects.filter(is_superuser=False)
    invites_list = ActiveInvites.objects.all()
    context = {
        'title': 'Управление пользователями',
        'objects_list': objects_list,
        'invites_list': invites_list,
    }
    return render(request, template_name, context=context)


@login_required
def toggle_user_active_view(request, pk):
    # Проверка привилегий
    if not request.user.is_superuser:
        raise Http404
    # Меняем активность
    user = get_object_or_404(User, pk=pk)
    user.is_active = not user.is_active
    user.save()
    return redirect('users:manage_users')


class GenerateInviteView(LoginRequiredMixin, View):
    template_name = 'admin/generate_invite.html'
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
        # Извлекаем ссылку из запроса
        project_url = request.POST.get("current-url")
        # Генерируем значение инвайта
        invite_number = self.__gen_invite_number()
        # Склеиваем значение со ссылкой
        registration_url = project_url + 'user/register/?invite=' + invite_number
        # Сохраняем значение в базу данных 
        record_object = self.model(invite_number=invite_number, invite_url=registration_url)
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


@login_required
def invite_details_view(request, pk):
    # Проверка привилегий
    if not request.user.is_superuser:
        raise Http404
    invite_record = get_object_or_404(ActiveInvites, pk=pk)
    template_name = 'admin/invite_details.html'
    context = {
        'invite': invite_record,
    }
    return render(request, template_name, context=context)


@login_required
def delete_invite_view(request, pk):
    # Проверка привилегий
    if not request.user.is_superuser:
        raise Http404
    invite_record = get_object_or_404(ActiveInvites, pk=pk)
    invite_record.delete()
    return redirect('users:manage_users')
