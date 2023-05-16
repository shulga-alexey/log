from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'status', 'producer_teacher',
                    'updated', 'created']
    list_filter = ['status', 'producer_teacher', 'updated', 'created']
    search_fields = ['title', 'text']
    prepopulated_fields = {'slug': ('title', 'producer_teacher')}
    ordering = ['status', 'producer_teacher', 'updated', 'created']
