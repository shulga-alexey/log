from django.conf import settings
from django.db import models


class Teacher(models.Model):
    user = models.OneToOneField(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE
        )
    slug = models.SlugField(
            unique=True
        )


class Student(models.Model):
    user = models.OneToOneField(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE
        )
    slug = models.SlugField(
            unique=True
        )
    teacher = models.ForeignKey(
            'Teacher',
            on_delete=models.SET_NULL,
            related_name='students',
            blank=True,
            null=True
        )
    group = models.ForeignKey(
            'StudentGroup',
            on_delete=models.SET_NULL,
            related_name='students',
            blank=True,
            null=True
        )


class StudentGroup(models.Model):
    title = models.CharField(
            max_length=250
        )
    slug = models.SlugField(
            unique=True
        )
    description = models.TextField()

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
