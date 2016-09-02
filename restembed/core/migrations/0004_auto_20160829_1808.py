# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_savedembeds_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savedembeds',
            name='author_name',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='savedembeds',
            name='author_url',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='savedembeds',
            name='height',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='savedembeds',
            name='html',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='savedembeds',
            name='thumbnail_height',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='savedembeds',
            name='thumbnail_url',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='savedembeds',
            name='thumbnail_width',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='savedembeds',
            name='width',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
