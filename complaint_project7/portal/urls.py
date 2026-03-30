from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('file/', views.file_complaint, name='file'),
    path('track/', views.track_status, name='track'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('officer-login/', views.officer_login, name='officer_login'),
    path('officer-dashboard/', views.officer_dashboard, name='officer_dashboard'),
    path('logout/', views.officer_logout, name='logout'),
]