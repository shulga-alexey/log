from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path(
            'students/<int:student_id>/',
            views.student_detail,
            name='student_detail'
        ),
    path(
            'teachers/<int:teacher_id>/',
            views.teacher_detail,
            name='teacher_detail'
        ),
]
