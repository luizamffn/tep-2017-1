# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-31 01:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0003_auto_20170731_0157'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bloqueado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bloqueado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bloqueios_recebidos', to='perfis.Perfil')),
                ('solicitante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bloqueios_feitos', to='perfis.Perfil')),
            ],
        ),
    ]
