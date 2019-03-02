from django.urls import path
from . import views

app_name = 'pets'

urlpatterns = [
    path('get_pet_info', views.get_pet_info, name='get_pet_info'),
]