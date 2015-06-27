# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prompt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mc_campaign_id', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='list',
            name='mc_list_id',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
