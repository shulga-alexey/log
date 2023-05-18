from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path(
            '<int:task_id>/',
            views.task_detail,
            name='task_detail'
        ),
    path(
            'task_group/<int:task_group_id>/',
            views.task_group,
            name='task_group'
        ),
]
