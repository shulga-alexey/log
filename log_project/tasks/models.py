from django.conf import settings
from django.db import models


class Teacher(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)


class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    tasks = models.ManyToManyField('Task',
                                   through='AppointedTask',
                                   through_fields=('student', 'task'))
    group = models.ForeignKey('StudentsGroup',
                              on_delete=models.SET_NULL,
                              related_name='students',
                              blank=True,
                              null=True)


class StudentsGroup(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Task(models.Model):

    class Status(models.TextChoices):
        REJECTED = 'RJ', 'Rejected'
        ACCEPTED = 'AC', 'Accepted'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    text = models.TextField()
    producer_teacher = models.ForeignKey('Teacher',
                                         on_delete=models.CASCADE,
                                         related_name='tasks')
    students = models.ManyToManyField('Student',
                                      through='AppointedTask',
                                      through_fields=('task', 'student'))
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.REJECTED)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class AppointedTask(models.Model):
    task = models.ForeignKey('Task',
                             on_delete=models.CASCADE,
                             related_name='appointed')
    student = models.ForeignKey('Student',
                                on_delete=models.CASCADE)
    appointor_teacher = models.ForeignKey(Teacher,
                                          on_delete=models.CASCADE)
    date = models.DateTimeField()
