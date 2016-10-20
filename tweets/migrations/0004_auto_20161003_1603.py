# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0003_auto_20160930_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='retweet',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='content',
            field=models.CharField(max_length=140, blank=True),
        ),
    ]
