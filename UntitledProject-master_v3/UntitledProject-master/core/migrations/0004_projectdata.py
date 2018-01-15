# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-16 04:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20170915_2041'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data', to='core.Project')),
            ],
        ),
    ]