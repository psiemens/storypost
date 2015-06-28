# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_user_lists'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mc_api_key',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
