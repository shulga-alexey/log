from django.db import models

from users.models import Teacher, Student


class Task(models.Model):

    class Status(models.TextChoices):
        REJECTED = 'RJ', 'Rejected'
        ACCEPTED = 'AC', 'Accepted'

    title = models.CharField(
            max_length=250
        )
    slug = models.SlugField(
            max_length=250
        )
    status = models.CharField(
            max_length=2,
            choices=Status.choices,
            default=Status.REJECTED
        )
    producer_teacher = models.ForeignKey(
            Teacher,
            related_name='produced_tasks',
            on_delete=models.CASCADE
        )
    appointor_teachers = models.ManyToManyField(
            Teacher,
            related_name='appointor_tasks',
            through='AppointedTask',
            through_fields=('task', 'appointor_teacher'),
        )
    students = models.ManyToManyField(
            Student,
            related_name='tasks',
            through='AppointedTask',
            through_fields=('task', 'student'),
        )
    created = models.DateTimeField(
            auto_now_add=True
        )
    updated = models.DateTimeField(
            auto_now=True
        )
    text = models.TextField()

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class AppointedTask(models.Model):
    task = models.ForeignKey(Task,
                             on_delete=models.CASCADE)
    student = models.ForeignKey(Student,
                                on_delete=models.CASCADE)
    appointor_teacher = models.ForeignKey(Teacher,
                                          on_delete=models.CASCADE)
    date = models.DateTimeField()
