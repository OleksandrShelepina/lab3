from django.urls import path, include

urlpatterns = [
    path('', include('main.urls')),  # якщо додаток називається main
]


urlpatterns = [
    path('', views.home, name='home'),
    path('view1/', views.view1, name='view1'),
    path('view2/', views.view2, name='view2'),
    path('view3/', views.view3, name='view3'),
    path('view4/', views.view4, name='view4'),
    path('view5/', views.view5, name='view5'),
]
