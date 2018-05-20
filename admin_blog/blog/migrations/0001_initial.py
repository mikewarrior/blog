# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-20 13:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=40)),
                ('content', models.TextField()),
                ('creation_date', models.DateField(auto_now=True)),
                ('publish_date', models.DateField(auto_now=True)),
            ],
        ),
    ]
