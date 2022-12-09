from django.urls import path
from Auth import views

urlpatterns = [
    path('login', views.loginView, name='Login'),
    path('register', views.registerView, name='Register'),
]