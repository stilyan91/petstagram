from django.urls import path, include

from Petstagram.accounts import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.logout_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/<int:pk>/', include([
        path('', views.profile_details, name='profile-details'),
        path('edit/', views.edit_profile, name='profile-edit'),
        path('delete/', views.delete_profile, name='profile-delete'),
    ])),

]
