# Generated by Django 3.2.4 on 2021-06-08 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sellers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=120)),
                ('document', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SellerData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=30)),
                ('seller_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sellers.sellers')),
            ],
        ),
    ]
