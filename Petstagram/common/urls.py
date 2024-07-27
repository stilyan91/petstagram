from django.urls import path
from .views import index, like_functionality, copy_link_to_clipboard, comment_functionality

urlpatterns = [
    path('', index, name='index'),
    path('like/<int:photo_id>/', like_functionality, name='like'),
    path('share/<int:photo_id>/', copy_link_to_clipboard, name='share'),
    path('comment/<int:photo_id>', comment_functionality, name='comment' )
]
