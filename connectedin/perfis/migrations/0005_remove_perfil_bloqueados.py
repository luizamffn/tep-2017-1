# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-31 02:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0004_bloqueado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='bloqueados',
        ),
    ]