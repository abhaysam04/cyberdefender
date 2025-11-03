from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('alerts/', views.alerts, name='alerts'),
    path('add/', views.add_alert, name='add_alert'),
    path('register/', views.register, name='register'),
    path('delete/<int:alert_id>/', views.delete_alert, name='delete_alert'),
		
]
