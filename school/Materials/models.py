from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Material(models.Model):
    MATERIAL_TYPES = [
        ('file', 'File'),
        ('link', 'Link'),
        ('video', 'Video'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    file = models.FileField(upload_to='materials/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    youtube_url = models.URLField(blank=True, null=True)

    material_type = models.CharField(max_length=10, choices=MATERIAL_TYPES)

    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title