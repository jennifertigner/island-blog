# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-07 21:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_auto_20160407_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_text',
            field=models.TextField(null=True),
        ),
    ]
