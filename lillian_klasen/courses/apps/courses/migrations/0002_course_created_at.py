# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-19 22:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='1976-12-12 00:00:00'),
            preserve_default=False,
        ),
    ]
