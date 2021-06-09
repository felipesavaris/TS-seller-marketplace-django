from os import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.list_sellers, name='list_sellers'),
    path('new_seller/', views.create_seller, name='create_seller'),
    path('update/<int:id>', views.update_seller, name='update_seller'),
    path('delete/<int:id>', views.delete_seller, name='delete_seller'),
]