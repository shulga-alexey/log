from django.views import generic

from .models import Task, TaskGroup


class TaskDetailView(generic.DetailView):
    model = Task


class TaskGroupDetailView(generic.DetailView):
    model = TaskGroup
