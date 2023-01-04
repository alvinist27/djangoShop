"""Module containing Celery tasks for the app_users application."""

from celery import shared_task
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail

User = get_user_model()


@shared_task(bind=True)
def send_mail_notification(self) -> str:
    """Celery task for sending Email notification to registered users.

    Returns:
        Task status.
    """
    users = User.objects.all()
    for user in users:
        mail_subject = 'Давно вас не было в уличных гонках'
        message = 'Заходите на .SHOP Появились новые товары для Вашего гардероба'

        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
            fail_silently=True,
        )
    return 'Done'
