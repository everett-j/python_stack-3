# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-08-19 18:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0003_auto_20190819_1816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='title',
        ),
    ]
