# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('heading', models.CharField(max_length=50)),
                ('content', models.TextField(blank=True)),
                ('hashtag', models.CharField(max_length=10, blank=True)),
                ('posted_on', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
