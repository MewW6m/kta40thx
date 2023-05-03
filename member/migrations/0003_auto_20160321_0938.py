# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-21 00:38
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_auto_20160318_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberlist',
            name='image',
            field=models.ImageField(blank=True, help_text='画像は任意で', storage=django.core.files.storage.FileSystemStorage(location='kta40thx/static/media/memberphoto'), upload_to='memberphoto', verbose_name='画像'),
        ),
    ]