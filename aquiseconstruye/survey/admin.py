from django.contrib import admin
from .models import *
# Register your models here.
class SurveyAdmin(admin.ModelAdmin):
    list_display = ('survey',)
    ordering = ["created_at"]

admin.site.register(Survey, SurveyAdmin)