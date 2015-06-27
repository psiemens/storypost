# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mc_list_id', models.CharField(max_length=255, null=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
    ]
