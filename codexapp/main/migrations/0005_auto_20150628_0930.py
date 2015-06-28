# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_user_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prompt',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='reply',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
