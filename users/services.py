from django.conf import settings
from django.core.mail import send_mail


def send_register_verification_email(email, activation_link):
    subject = 'Calcoo: подтверждение регистрации'
    message = (
        f'Для подтверждения адреса электронной почты пройдите по ссылке:\n'
        f'{activation_link}'
    )
    send_email(email, subject, message)


def send_register_success_email(email):
    subject = 'Calcoo: успешная регистрация пользователя сервисе'
    message = (
        'Ваш аккаунт активирован'
    )
    send_email(email, subject, message)


def send_email(email, subject: str, message: str):
    send_mail (
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email, ],
    )
