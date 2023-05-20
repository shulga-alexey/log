from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path(
            '<int:pk>/',
            views.TaskDetailView.as_view(),
            name='task_detail'
        ),
    path(
            'task_group/<int:pk>/',
            views.TaskGroupDetailView.as_view(),
            name='task_group'
        ),
]
