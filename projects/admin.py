from django.contrib import admin
from projects.models import Projects

# Register your models here.



class ProjectAdmin(admin.ModelAdmin):
  list_display = ['project','create_at','status']
  list_filter = ['status']

admin.site.register(Projects, ProjectAdmin)