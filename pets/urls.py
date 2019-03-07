from django.urls import path
from . import views

app_name = 'pets'

urlpatterns = [
    path('get_pet_info', views.get_pet_info, name='get_pet_info'),
    path('publish_pet_information', views.publish_pet_information, name='publish_pet_information'),
    path('modify/', views.modify, name='modify'),
    path('delete/', views.delete, name='delete'),

    path('get_recommand_pets', views.get_recommand_pets, name='get_recommand_pets'),
]
