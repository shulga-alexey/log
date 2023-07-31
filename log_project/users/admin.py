from django.contrib import admin

from .models import Student, StudentGroup, Teacher


@admin.register(Teacher)
class TaskAdmin(admin.ModelAdmin):

    list_display = ('user',)
    search_fields = ('user',)
    ordering = ('user',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    list_display = ('user', 'group')
    list_filter = ('group',)
    search_fields = ('user', 'group')
    ordering = ('user',)


@admin.register(StudentGroup)
class StudentGroupAdmin(admin.ModelAdmin):

    list_display = ('title', 'slug')
    search_fields = ('title', 'description')
    ordering = ('title',)
