from django.contrib import admin
from projects.models import Project, Technology

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Project, ProjectAdmin)
admin.site.register(Technology, ProjectAdmin)