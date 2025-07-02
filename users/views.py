from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, UpdateView
from users.forms import UserRegisterForm, UserLoginForm, UserUpdateForm
from users.models import User


def user_register_view(request):
    form = UserRegisterForm()
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
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
            user = authenticate(email=cleaned_data['email'], password=cleaned_data['password'])
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
