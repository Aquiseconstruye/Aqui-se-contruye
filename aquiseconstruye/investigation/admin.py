from django.contrib import admin
from .models import *
from tinymce.widgets import TinyMCE
# Register your models here.


class InvestigationAdmin(admin.ModelAdmin):

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }
class InvestigationHomeAdmin(admin.ModelAdmin):

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }
admin.site.register(Investigation,InvestigationAdmin)
admin.site.register(InvestigationHome,InvestigationHomeAdmin)