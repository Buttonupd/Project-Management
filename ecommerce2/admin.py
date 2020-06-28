from django.contrib import admin
from .models import Project
from .models import Task

class ProjectAdmin(admin.ModelAdmin):
    raw_id_fields = ('cohort',)
    list_display = ['name', 'cohort',]
    list_filter = ['name', 'cohort',]
    search_fields = ['name', 'cohort', 'status',]
    prepopulated_fields = {'slug': ('name', )}

    class Meta:
        model = Project


class TaskAdmin(admin.ModelAdmin):
    list_display = ['task_name', 'project',]
    list_filter = ['project',]
    search_fields = ['project',]

admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)

 