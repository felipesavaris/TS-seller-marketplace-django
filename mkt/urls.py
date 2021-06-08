from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='marketplace-list'),
    path('create/mkt', views.new_mkt, name='mkt-add')

]