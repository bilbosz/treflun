from django.urls import path
from accounts import views

urlpatterns = [
    path('login', views.do_login, name='login'),
    path('authenticate', views.do_auth, name='do_auth')
]
