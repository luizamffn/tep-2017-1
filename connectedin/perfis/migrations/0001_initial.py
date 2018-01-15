# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-29 03:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Convite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('imagem', models.ImageField(default='perfil/person.png', null=True, upload_to='perfil/')),
                ('telefone', models.CharField(max_length=255)),
                ('nome_empresa', models.CharField(max_length=255)),
                ('ativo', models.BooleanField(default=True)),
                ('justificativa', models.CharField(max_length=255)),
                ('pergunta', models.CharField(max_length=255)),
                ('resposta', models.CharField(max_length=255)),
                ('bloqueados', models.ManyToManyField(related_name='_perfil_bloqueados_+', to='perfis.Perfil')),
                ('contatos', models.ManyToManyField(related_name='_perfil_contatos_+', to='perfis.Perfil')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='perfil', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Postagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField(max_length=1000)),
                ('data', models.DateField(null=True)),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postagens', to='perfis.Perfil')),
            ],
        ),
        migrations.AddField(
            model_name='convite',
            name='convidado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='convites_recebidos', to='perfis.Perfil'),
        ),
        migrations.AddField(
            model_name='convite',
            name='solicitante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='convites_feitos', to='perfis.Perfil'),
        ),
    ]