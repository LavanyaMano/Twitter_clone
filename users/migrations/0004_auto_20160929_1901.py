# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='follow',
            field=models.ManyToManyField(related_name='followed_by', to='users.Profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.URLField(default='https://app.nimia.com/static/img/default_profile.png'),
        ),
    ]
