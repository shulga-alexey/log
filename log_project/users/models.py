from django.conf import settings
from django.db import models


class Teacher(models.Model):
    user = models.OneToOneField(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE
        )


class Student(models.Model):
    user = models.OneToOneField(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE
        )
    group = models.ForeignKey(
            'StudentsGroup',
            on_delete=models.SET_NULL,
            related_name='students',
            blank=True,
            null=True
        )


class StudentsGroup(models.Model):
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
