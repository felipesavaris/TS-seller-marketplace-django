from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView
)
from mkt.models import Marketplace


from .forms import MarketplaceForm


home = ListView.as_view(template_name='mkt_list.html',
                        model=Marketplace)


new_mkt = CreateView.as_view(template_name='add_mkt.html',
                             form_class=MarketplaceForm,
                             model=Marketplace)