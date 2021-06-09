from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, IntegerField
from django.db.models.fields.related import ForeignKey
from django.shortcuts import resolve_url as r


class Sellers(models.Model):

    name = models.CharField(max_length=30)
    last_name = CharField(max_length=50)
    email = CharField(max_length=120)
    document = IntegerField()

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return r('list_sellers')

class SellerData(models.Model):

    seller_id = ForeignKey(Sellers, on_delete=CASCADE)
    address = CharField(max_length=100)
    number = IntegerField()
    city = CharField(max_length=50)
    state = CharField(max_length=30)

    def __str__(self):
        return self.seller_id
