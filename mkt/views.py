from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    UpdateView
)

from django.urls import reverse_lazy as r
 
from mkt.models import Marketplace, Configuration


from .forms import MarketplaceForm, ConfigurationForm

home = ListView.as_view(template_name='mkt_list.html',
                        model=Marketplace)


new_mkt = CreateView.as_view(template_name='add_mkt.html',
                             form_class=MarketplaceForm,
                             model=Marketplace)


class MktDeleteView(DeleteView):
    template_name = 'mkt_delete.html'
    model = Marketplace
    success_url = r('marketplace-list')


update_mkt = UpdateView.as_view(template_name='update_mkt.html',
                                model=Marketplace,
                                form_class=MarketplaceForm)


list_config = ListView.as_view(template_name='configuration_list.html',
                               model=Configuration)


new_config = CreateView.as_view(template_name='add_configuration.html',
                                form_class=ConfigurationForm,
                                model=Configuration)


class ConfigDeleteView(DeleteView):
    template_name = 'conf_delete.html'
    model = Configuration
    success_url = r('config-list')


update_config = UpdateView.as_view(template_name='update_mkt.html',
                                   model=Configuration,
                                   form_class=ConfigurationForm)
