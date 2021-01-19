from django.contrib import admin
from home.models import Settings,About

# Register your models here.

admin.site.register(Settings)

class AboutAdmin(admin.ModelAdmin):
  list_display = ['title','create_at','status']
  list_filter = ['status']

admin.site.register(About, AboutAdmin)