from django.conf import settings
from django.core.mail import send_mail


def send_register_verification_email(email, activation_link):
    subject = 'Calcoo: Подтверждение регистрации'
    message = (
        f'Для подтверждения регистрации на сервисе Calcoo пройдите по ссылке:\n'
        f'{activation_link}'
    )
    send_email(email, subject, message)


def send_register_success_email(email):
    subject = 'Calcoo: Успешная регистрация пользователя на сервисе'
    message = (
        'Ваш аккаунт активирован'
    )
    send_email(email, subject, message)


def send_password_recovery_email(email, recovery_url):
    subject = 'Calcoo: Запрос на восстановление пароля'
    message = (
        f'Для восстановения пароля на сервисе Calcoo пройдите по ссылке:\n'
        f'{recovery_url}'
    )
    send_email(email, subject, message)


def send_recovery_success_email(email):
    subject = 'Calcoo: успешное изменение пароля'
    message = (
        'Пароль успешно изменен!'
    )
    send_email(email, subject, message)


def send_email(email, subject: str, message: str):
    send_mail (
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email, ],
    )
