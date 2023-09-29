"""
URL configuration for TextUtil project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = "Home"),
    path('remove_punc', views.remove_punc, name = "remove_punc"),
    path('cap_first', views.cap_first, name = "Cap_first"),
    path('space_remove', views.remove_space, name = "Remove_Space"),
    path('new_line_remove', views.new_lineremove, name = "New_line remove"),
    path('char_count', views.char_count, name = "Character Count"),

]
