"""nautprofile URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from nautprofile.settings import STATIC_URL
from profiles import views
from django.conf import settings
from django.conf.urls.static import static


app_name="home"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('team/',views.team,name='team'),
    path('profile/<slug:slug>/edit',views.edit_profile,name='edit_profile'),
    path('profile/<slug:slug>',views.profile,name='profile'),
    path('profile/add/',views.add_profile,name='add_profile'),
    path('gallery/',views.add_gallery,name='add_gallery'),
    path('prompt/',views.prompt,name='prompt'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
