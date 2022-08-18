from django.urls import path
from . import views
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('', views.home),
    path('register/', views.register),
    path('login/', LoginView.as_view(template_name='account/login.html'), name="login"),
    path('profile/', views.view_profile),
    ]