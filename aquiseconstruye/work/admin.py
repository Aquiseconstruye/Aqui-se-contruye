from django.contrib import admin
from .models import *
# Register your models here.

class WorkAdmin(admin.ModelAdmin):
    list_display = ('name', 'traffic_light', 'official',)
    ordering = ["created_at"]


admin.site.register(Work, WorkAdmin)
