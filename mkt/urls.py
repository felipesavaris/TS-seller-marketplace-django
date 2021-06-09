from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='marketplace-list'),
    path('create/mkt', views.new_mkt, name='mkt-add'),
    path('<int:pk>/delete/mkt', views.MktDeleteView.as_view(),
         name='delete-mkt'),
    path('mkt/update/<int:pk>', views.update_mkt, name='mkt-update'),


    path('list-config',  views.list_config, name='config-list'),
    path('create/config', views.new_config, name='config-add'),
    path('<int:pk>/delete/config', views.ConfigDeleteView.as_view(),
         name='delete-config'),
    path('config/update/<int:pk>', views.update_config, name='config-update'),



]