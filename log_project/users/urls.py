from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path(
            'teachers/<str:username>/',
            views.TeacherDetailView.as_view(),
            name='teacher_detail'
        ),
    path(
            'students/<str:username>/',
            views.StudentDetailView.as_view(),
            name='student_detail'
        ),
]
