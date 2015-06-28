# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20150628_0930'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='lists',
            field=models.ManyToManyField(related_name='subscribed_user', to='main.List'),
        ),
    ]
