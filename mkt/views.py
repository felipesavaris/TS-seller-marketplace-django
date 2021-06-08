from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    UpdateView
)

from django.urls import reverse_lazy as r
 
from mkt.models import Marketplace


from .forms import MarketplaceForm


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
