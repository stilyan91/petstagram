from django.urls import path, include

from .views import pet_add, pet_details, edit_pet, delete_pet

urlpatterns = [
    path('add/', pet_add, name='pet_add'),
    path('<str:username>/pet/<slug:pet_name>/', include([
        path('', pet_details, name='pet_details'),
        path('edit/', edit_pet, name='edit_pet'),
        path('delete/', delete_pet, name='delete_pet'),
    ])),
]
