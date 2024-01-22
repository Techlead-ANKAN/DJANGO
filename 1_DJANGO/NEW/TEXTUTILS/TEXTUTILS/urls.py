"""
URL configuration for TEXTUTILS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
    path('', views.index, name = "index"),
    path('analyze', views.analyze, name = "analyze"),
#     path('rmpunc', views.remove_punc, name = "rm_punc"),
#     path('capfirst', views.capitalize_first, name = "cap_first"),
#     path('lineremove', views.line_remove, name = "ln_rm"),
#     path('spaceremove', views.space_remove, name = "space_rm"),
#     path('charcount', views.character_count, name = "char_count"),
]
