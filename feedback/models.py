from django.core.mail import send_mail
from django.db import models

from store.settings import EMAIL_HOST_USER
from users.models import User


class Feedback(models.Model):
    STATUS_CHOICES = [
        ('New', 'Новая'),
        ('In_progress', 'В работе'),
        ('Completed', 'Завершена'),
    ]
    RATING_CHOICES = [
        (1, 'Very Bad'),
        (2, 'Bad'),
        (3, 'Neutral'),
        (4, 'Good'),
        (5, 'Very Good'),
    ]
    TYPE_CHOICES = [
        ('Feedback', 'Отзыв'),
        ('Claim', 'Жалоба')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField(null=True, blank=True)
    rating = models.IntegerField(choices=RATING_CHOICES)
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='New',
    )


class KnowledgeBase(models.Model):
    CATEGORY_CHOICES = [
        ('general', 'General'),
        ('technical', 'Technical'),
        ('billing', 'Billing'),
        ('other', 'Other'),
    ]

    question = models.CharField(max_length=255)
    answer = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)


class ReferenceMaterial(models.Model):
    CONTENT_TYPE_CHOICES = [
        ('faq', 'FAQ'),
        ('instruction', 'Instruction'),
        ('guide', 'Guide'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=255)
    content_type = models.CharField(max_length=50, choices=CONTENT_TYPE_CHOICES)
    content = models.TextField()


class EmailSend(models.Model):

    def send_email(self):
        subject = f'Автоматическая рассылка справочных материалов'
        message = f'Справочные материалы'
        send_mail(
            subject=subject,
            message=message,
            from_email=EMAIL_HOST_USER,
            recipient_list=["danila.gromakov@gmail.com"],
            fail_silently=False,
        )