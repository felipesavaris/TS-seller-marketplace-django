from django import forms
from .models import SellerData, Sellers


class SellersForm(forms.ModelForm):
    class Meta:
        model = Sellers
        fields = '__all__'


class SellerDataForm(forms.ModelForm):
    class Meta:
        model = SellerData
        fields = '__all__'
