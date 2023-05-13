from django.db import models
from django.utils import timezone

from users.models import Teacher, Student


class Task(models.Model):

    class Status(models.TextChoices):
        REJECTED = 'RJ', 'Rejected'
        ACCEPTED = 'AC', 'Accepted'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    text = models.TextField()
    teacher = models.ForeignKey(Teacher,
                                on_delete=models.CASCADE,
                                related_name='tasks')
    students = models.ManyToManyField(Student,
                                      related_name='tasks')
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.REJECTED)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
