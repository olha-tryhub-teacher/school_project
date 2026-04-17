from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name="Назва")
    description = models.TextField(verbose_name="Опис")
    location = models.CharField(max_length=255, verbose_name="Локація")
    start_date = models.DateTimeField(verbose_name="Дата початку")
    end_date = models.DateTimeField(verbose_name="Дата завершення")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events', verbose_name="Автор")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Подія"
        verbose_name_plural = "Події"