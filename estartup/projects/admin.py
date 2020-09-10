from django.contrib import admin

# Register your models here.

from projects.models import Project
from projects.models import ProjectImage


admin.site.register(Project)
admin.site.register(ProjectImage)