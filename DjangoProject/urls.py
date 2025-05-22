from django.contrib import admin
from django.urls import path
from . import views  # Імпортуємо views.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Викликаємо функцію home з views.py
]
