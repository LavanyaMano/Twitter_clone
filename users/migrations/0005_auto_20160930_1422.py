# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20160929_1901'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('status', models.IntegerField(choices=[(1, 'Following'), (2, 'Blocked')])),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='follow',
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.CharField(max_length=200, blank=True, default='http://i164.photobucket.com/albums/u8/hemi1hemi/COLOR/COL9-6.jpg'),
        ),
        migrations.AddField(
            model_name='relationship',
            name='followed_by',
            field=models.ForeignKey(related_name='followed_by', to='users.Profile'),
        ),
        migrations.AddField(
            model_name='relationship',
            name='following',
            field=models.ForeignKey(related_name='following', to='users.Profile'),
        ),
        migrations.AddField(
            model_name='profile',
            name='relationships',
            field=models.ManyToManyField(through='users.Relationship', related_name='related_to', to='users.Profile'),
        ),
    ]
