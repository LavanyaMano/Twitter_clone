# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20160927_1755'),
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='profile',
            field=models.ForeignKey(null=True, to='users.Profile'),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='hashtag',
            field=models.CharField(max_length=20, blank=True),
        ),
    ]
