from django import forms 
from django.contrib.auth.forms import UserCreationForm
from users.models import User 


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(label='имя пользователя', widget=forms.TextInput(attrs={"class": "form-control form-control-user", "placeholder": "Ваше имя"}))
    last_name = forms.CharField(label='фамилия пользователя', widget=forms.TextInput(attrs={"class": "form-control form-control-user", "placeholder": "Ваша фамилия"}))
    email = forms.EmailField(label='email', widget=forms.EmailInput(attrs={"class": "form-control form-control-user", "placeholder": "Электронная почта"}))
    password1 = forms.CharField(label='пароль', widget=forms.PasswordInput(attrs={"class": "form-control form-control-user", "placeholder": "Пароль"}))
    password2 = forms.CharField(label='пароль', widget=forms.PasswordInput(attrs={"class": "form-control form-control-user", "placeholder": "Повторите пароль"}))

    class Meta:
        model = User 
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    email = forms.EmailField(label='email', widget=forms.EmailInput(attrs={"class": "form-control form-control-user", "placeholder": "Электронная почта"}))
    password = forms.CharField(label='пароль', widget=forms.PasswordInput(attrs={"class": "form-control form-control-user", "placeholder": "Пароль"}))


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'phone', 'telegram')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})
