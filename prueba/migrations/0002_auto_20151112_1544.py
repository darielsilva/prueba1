# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prueba', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='raza',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='animal',
            name='sexo',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]
