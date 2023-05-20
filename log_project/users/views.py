from django.shortcuts import get_object_or_404
from django.views import generic

from .models import Teacher, Student


class TeacherDetailView(generic.DetailView):
    model = Teacher

    def get_queryset(self, **kwargs):
        return get_object_or_404(self.model,
                                 user__username=kwargs.get('username'))


class StudentDetailView(generic.DetailView):
    model = Student

    def get_queryset(self, **kwargs):
        return get_object_or_404(self.model,
                                 user__username=kwargs.get('username'))
