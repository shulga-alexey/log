from django.contrib.auth.models import AbstractUser
from django.db import models


class Teacher(AbstractUser):
    """Пользователь «teacher»."""

    bio = models.TextField(
        null=True,
        blank=True,
        verbose_name='описание'
    )

    class Meta:
        ordering = ('username',)
        verbose_name = 'преподаватель'
        verbose_name_plural = 'преподаватели'


class Student(AbstractUser):
    """Пользователь «student»."""

    teacher = models.ForeignKey(
        'Teacher',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='students',
        verbose_name='преподаватель'
    )
    student_group = models.ForeignKey(
        'StudentGroup',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='students',
        verbose_name='учебная группа'
    )
    bio = models.TextField(
        null=True,
        blank=True,
        verbose_name='описание'
    )

    class Meta:
        ordering = ('username',)
        verbose_name = 'ученик'
        verbose_name_plural = 'ученики'


class StudentGroup(models.Model):
    title = models.CharField(
        unique=True,
        max_length=250,
        verbose_name='название'
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='слаг'
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='описание'
    )

    class Meta:
        ordering = ('title',)
        verbose_name = 'учебная группа'
        verbose_name_plural = 'учебные группы'

    def __str__(self):
        return self.title
