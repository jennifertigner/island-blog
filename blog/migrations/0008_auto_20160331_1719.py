# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-01 00:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20160331_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='filepath',
            field=models.ImageField(upload_to='images/'),
        ),
    ]