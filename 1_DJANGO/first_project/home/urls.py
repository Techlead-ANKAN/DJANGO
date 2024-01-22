from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
        path('', views.home, name = "Home"),
    path('about', views.about, name = "About"),
    path('services', views.services, name = "Service"),
    path('contacts', views.contacts, name = "Contact"),


    path('admin/', admin.site.urls),  # maps to admin page
]