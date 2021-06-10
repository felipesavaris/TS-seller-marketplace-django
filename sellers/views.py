from django import setup
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy as r
from .forms import SellerDataForm, SellersForm
from .models import Sellers


def list_sellers(request):
    sellers = Sellers.objects.all()
    return render(request, 'sellers.html', {'sellers': sellers})


def create_seller(request):
    form = SellersForm(request.POST or None)
    if form.is_valid():
        form.save()
        # return HttpResponseRedirect('')
        sellers = Sellers.objects.all()
        return render(request, 'sellers.html', {'sellers': sellers})
    return render(request, 'create_seller.html', {'form': form})
    

def update_seller(request, id):
    seller = Sellers.objects.get(id=id)
    form = SellersForm(request.POST, instance=seller)
    if form.is_valid():
        form.save()
        return redirect('list_sellers')
    return render(request, 'update_seller.html', {'seller': seller})


def delete_seller(request, id):
    form = Sellers.objects.get(id=id)
    form.delete()
    # sellers = Sellers.objects.all()
    return redirect('list_sellers')


def seller_data(request, seller_id):  # PAREI AQUI (PRECISO VER COMO FAZ PARA LISTAR DATA PELO ID DO SELLER)
    print('----------------------------')
    print(seller_id, type(seller_id))
    print('----------------------------')
    seller = Sellers.pk(id=seller_id)
    data = request.POST
    data['seller_id'] = seller
    form = SellerDataForm(data or None)
    if form.is_valid():
        form.save()
        return redirect('seller_address')
    return render(request, 'seller_address.html', {'form': form})
