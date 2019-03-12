from django.urls import path
from . import views

app_name = 'pets'

urlpatterns = [
    path('get_pets_of_user', views.get_pets_of_user, name='get_pets_of_user'),
    path('publish_pet_information', views.publish_pet_information, name='publish_pet_information'),
    path('modify/', views.modify, name='modify'),
    path('delete/', views.delete, name='delete'),
    path('petfilter', views.petfilter, name='petfilter'),
    path('get_recommand_pets', views.get_recommand_pets, name='get_recommand_pets'),
    path('get_pet_info_from_id', views.get_pet_info_from_id, name='get_pet_info_from_id'),
]
