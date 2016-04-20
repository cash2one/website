# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-18 16:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0012_auto_20160417_1247'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ShowEpisodePage',
            new_name='ShowAudioSeriesEpisodePage',
        ),
        migrations.RenameModel(
            old_name='ShowEpisodeIndexPage',
            new_name='ShowAudioSeriesIndexPage',
        ),
        migrations.AlterModelOptions(
            name='showaudioseriesepisodepage',
            options={'verbose_name': 'Show Audio Stream Episode'},
        ),
        migrations.AlterModelOptions(
            name='showaudioseriesindexpage',
            options={'verbose_name': 'Show Audio Series Listing'},
        ),
    ]