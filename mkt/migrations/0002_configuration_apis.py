# Generated by Django 3.2.4 on 2021-06-08 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mkt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration',
            name='apis',
            field=models.URLField(default=1, verbose_name='API'),
            preserve_default=False,
        ),
    ]