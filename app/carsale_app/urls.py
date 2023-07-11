from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from .views import login_view, register

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/login/', login_view, name='login'),
    path('accounts/register/', register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('home/', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('catalog/', views.catalog, name='catalog'),
    path('sell/', views.sell_car, name='sell_car'),
    path('checkout', views.checkout, name='checkout'),
    path('success', views.success, name='success'),
]