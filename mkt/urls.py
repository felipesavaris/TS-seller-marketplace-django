from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='marketplace-list'),
    path('create/mkt', views.new_mkt, name='mkt-add'),
    path('<int:pk>/delete/mkt', views.MktDeleteView.as_view(),
         name='delete-mkt'),
    path('mkt/update/<int:pk>', views.update_mkt, name='mkt-update'),



]