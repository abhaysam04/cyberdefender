from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('alerts/', views.alerts, name='alerts'),
    path('add/', views.add_alert, name='add_alert'),
    path('check-ip/', views.check_ip, name='check_ip'),		
]
