from django.urls import path, include
from .views import photo_add, photo_edit, photo_details
urlpatterns = [
    path('add/', photo_add, name='photo_add'),
    path('<int:pk>/', include([
        path('',  photo_details, name='photo_details'),
        path('edit/', photo_edit, name='photo_edit'),
    ])),
]
