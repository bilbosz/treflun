from django.contrib.auth.views import LoginView
from django.urls import path
from accounts import views

urlpatterns = [
    path('login', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('register', views.do_register, name='register')
]
