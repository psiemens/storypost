# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20150628_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='points',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='lists',
            field=models.ManyToManyField(related_name='subscribers', to='main.List'),
        ),
    ]
