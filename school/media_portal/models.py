from django.db import models

# Create your models here.

class Classroom(models.Model):
    number = models.IntegerField(max_length=2)
    letter = models.CharField(max_length=1)

    def __str__(self):
        return f"{self.number}-{self.letter}"

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    classroom = models.ForeignKey(Classroom, on_delete=models.SET_NULL, null=True, related_name='students')
    STATUS_CHOICES = [
        ("teacher", "Teacher"),
        ("student", "Student"),
    ]
    status = models.CharField(choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.status} - {self.last_name} {self.first_name}, {self.classroom}"
