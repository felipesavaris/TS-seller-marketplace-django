from django.db import models
from django.shortcuts import resolve_url as r


class Marketplace(models.Model):
    name = models.CharField('Nome', max_length=150)
    description = models.CharField('Descrição', max_length=255)
    contact_phone = models.CharField('Telefone', max_length=14)
    contact_email = models.EmailField('E-mail', max_length=120)
    website = models.URLField('website', blank=True)
    technical_manager = models.CharField('Responsável técnico', max_length=255)

    class Meta:
        verbose_name_plural = 'Marketplaces'
        verbose_name = 'Marketplace'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return r('marketplace-list')


class Configuration(models.Model):
    configuration = models.ForeignKey('Marketplace', on_delete=models.CASCADE,
                                      related_name='marketplace')
    endpoint = models.URLField('Endpoint')
    secret_key = models.CharField(max_length=255)
