# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-07 23:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='the_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gallery.GalleryImage'),
        ),
    ]
