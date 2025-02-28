# home/urls.py
from django.urls import path
from. import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/create_account/', views.create_account_view, name='create_account'),
    path('about/', views.about, name='about'),
    path('dashboards/', views.dashboards, name='dashboards'),
]