# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('usuario', models.CharField(max_length=9)),
                ('contrasena', models.CharField(max_length=9)),
                ('nombre', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('direccion', models.CharField(max_length=100)),
                ('comuna', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=20)),
                ('encontrado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=20)),
                ('animal', models.CharField(max_length=10)),
                ('codigofoto', models.CharField(max_length=15)),
                ('id_amo', models.ForeignKey(to='prueba.Amo')),
            ],
        ),
    ]
