from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('login', views.accounts_login, name='login'),
    path('register', views.accounts_register, name='register'),
    path('logout', views.accounts_logout, name='logout'),
    path('status', views.status, name='status'),
    path('get_user_info', views.get_user_info, name='get_user_info'),
    path('modify', views.accounts_modify, name='modify'),
]
