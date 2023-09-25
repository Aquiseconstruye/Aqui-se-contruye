from django.contrib import admin
from .models import *
from tinymce.widgets import TinyMCE
# Register your models here.

class MetodologicAdmin(admin.ModelAdmin):

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

class WhoweareAdmin(admin.ModelAdmin):

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }
admin.site.register(Whoweare, WhoweareAdmin)
admin.site.register(IntroAquiSeConstruye)
admin.site.register(Metodologic, MetodologicAdmin)