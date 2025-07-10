from django.db import models

# my imports 
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=50, verbose_name='Имя', blank=True, null=True)
    last_name = models.CharField(max_length=50, verbose_name='Фамилия', blank=True, null=True)
    email = models.EmailField(unique=True, verbose_name='Email')
    phone = models.CharField(max_length=12, unique=True ,verbose_name='Номер телефона', blank=True, null=True)
    telegram = models.CharField(max_length=150, unique=True, verbose_name='Telegram', blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name='Активность')
    invite_number = models.CharField(max_length=50, verbose_name='Инвайт', blank=True, null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['id']


class ActiveInvites(models.Model):
    invite_number = models.CharField(max_length=50, verbose_name='Инвайт', blank=True, null=True) 

    def __str__(self):
        return f'{self.invite_number}'

    class Meta:
        verbose_name = 'Инвайт'
        verbose_name_plural = 'Инвайты'
