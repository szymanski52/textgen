from django.urls import include, path
from django.contrib.auth import views as auviews

from . import views


urlpatterns = [
    path('registration/', views.register, name='register'),
    path('', views.home, name='home'),
    path('login/', auviews.LoginView.as_view(template_name='eventsmanager/login.html'), name='login'),
    path('logout/', auviews.LogoutView.as_view(template_name='eventsmanager/home.html'), name='logout'),
    path('goals/add/', views.goalsRedirect, name='goals_add'),
    path('goals/', views.showGoalsTable, name='goals'),
]