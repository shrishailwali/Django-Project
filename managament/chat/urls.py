from django.urls import path
from .import views

urlpatterns = [
    path('create/', views.chat_create, name='chat_create'),
    path('', views.chat_list, name='chat_list'),
    path('chat/<int:id>/edit/', views.chat_update, name='chat_update'),
    path('chat/<int:id>/delete/', views.chat_delete, name='chat_delete'),
    path('register/', views.register, name='register'),
    # path('search/', views.search_list, name ='search_list')
]