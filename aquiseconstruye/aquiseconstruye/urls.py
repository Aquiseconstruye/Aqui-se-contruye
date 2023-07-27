"""aquiseconstruye URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from work.views import ObrasView,ObraDetailView, download_files
from django.urls import re_path
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('team.urls')),
    path('', include('users.urls')),
    path('', include('work.urls')),
    path('', include('survey.urls')),
    path('', include('investigation.urls')),
    path('obras/',ObrasView.as_view(), name='obras'),
    path('obra/<str:slug>/',ObraDetailView.as_view(), name='obra'),
    path('obra/<slug:slug>/download/', download_files, name='download_files'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    #path('obra/<str:slug>/',WorkDetailView.as_view(), name='obra'),
    #url(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)