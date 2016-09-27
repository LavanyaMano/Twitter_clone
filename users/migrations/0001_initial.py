# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('bio', models.TextField(blank=True)),
                ('location', models.TextField(blank=True)),
                ('birthday', models.DateField(blank=True)),
            ],
        ),
    ]
