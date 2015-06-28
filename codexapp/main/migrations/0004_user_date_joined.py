# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 28, 5, 37, 45, 867291, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
