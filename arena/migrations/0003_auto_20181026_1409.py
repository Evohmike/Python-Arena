# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-26 11:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arena', '0002_profile_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author_name',
            field=models.CharField(default='Anonymous', max_length=50),
        ),
    ]
