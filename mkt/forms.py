from django import forms
from mkt.models import Marketplace, Configuration


class MarketplaceForm(forms.ModelForm):
    class Meta:
        model = Marketplace
        fields = '__all__'

        widgets = {
            'website': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_email': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'technical_manager': forms.TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'website': "Site",
            'contact_email': "E-mail",
            'contact_phone': "Telefone",
            'name': "Nome",
            'description': "Descrição",
            'technical_manager': "Responsável técnico",
        }


class ConfigurationForm(forms.ModelForm):
    class Meta:
        model = Configuration
        fields = '__all__'

        widgets = {
            'endpoint': forms.TextInput(attrs={'class': 'form-control'}),
            'secret_key': forms.TextInput(attrs={'class': 'form-control'}),
            'apis': forms.TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'endpoint': "Endpoint",
            'secret_key': "Secret_key",
            'apis': "Apis",
        }
