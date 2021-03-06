# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-08 18:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('edad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Obra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ObrasArte.Artista')),
            ],
        ),
        migrations.CreateModel(
            name='Pintura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_pintura', models.CharField(default='pinturaa', max_length=30)),
                ('estilo', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='obra',
            name='pintura',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ObrasArte.Pintura'),
        ),
        migrations.AddField(
            model_name='artista',
            name='pinturas',
            field=models.ManyToManyField(through='ObrasArte.Obra', to='ObrasArte.Pintura'),
        ),
    ]
