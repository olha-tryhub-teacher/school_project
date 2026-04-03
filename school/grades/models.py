from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Teacher(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    subjects = []
    students = []

    def __str__(self):
        return self.name

    def add_subject(self, subject):  # додає предмет
        self.subjects.append(subject)

    def add_subjects(self, subject=()):  # додає декілька предметів
        self.subjects.append(subject)

    def remove_subject(self, subject):  # видаляє предмет
        self.subjects.remove(subject)

    def remove_subjects(self, subject=()):  # видаляє декілька предметів
        self.subjects.remove(subject)

    def add_student(self, student):  # додає студента
        self.students.append(student)

    def add_students(self, student=()):  # додає декілька студентів
        self.students.append(student)

    def remove_student(self, student):  # видаляє студента
        self.students.remove(student)

    def remove_students(self, student=()):  # видаляє декілька студентів
        self.students.remove(student)

    def clear_subjects(self):
        self.subjects = []

    def clear_students(self):
        self.students = []

    def clear(self):
        self.subjects = []
        self.students = []

class Student(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Subject(models.Model):
    #teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)
    #student = models.ForeignKey(Student, on_delete=models.PROTECT)
    name = models.CharField(max_length=20)

class Grade(models.Model):
    grade = models.IntegerField(min_value=0)