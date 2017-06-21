# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-20 06:55
from __future__ import unicode_literals

from django.db import migrations, models
import shortener.validators


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0003_auto_20170618_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kirrurl',
            name='url',
            field=models.CharField(max_length=220, validators=[shortener.validators.validate_url]),
        ),
    ]