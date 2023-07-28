from django.contrib import admin
from .models import *
# Register your models here.

class WorkAdmin(admin.ModelAdmin):
    list_display = ('alias', 'traffic_light', 'official',)
    ordering = ["-created_at"]


class TrafficLightAdmin(admin.ModelAdmin):
    list_display = ('color',)
    ordering = ["color"]







admin.site.register(Work, WorkAdmin)

admin.site.register(TrafficLight,TrafficLightAdmin)
