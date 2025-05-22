from django.shortcuts import render
from .models import GamingMouse  # Якщо модель у цьому додатку
# Якщо модель у додатку app1, тоді заміни на:
# from app1.models import GamingMouse

def home(request):
    mice = GamingMouse.objects.all()  # Отримуємо всі мишки з БД
    return render(request, 'home.html', {'mice': mice})

def view1(request):
    return render(request, 'view1.html')

def view2(request):
    return render(request, 'view2.html')

def view3(request):
    return render(request, 'view3.html')

def view4(request):
    return render(request, 'view4.html')

def view5(request):
    return render(request, 'view5.html')

