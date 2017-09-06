# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-27 12:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='post_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='posts',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]
