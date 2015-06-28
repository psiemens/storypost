# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_user_mc_api_key'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mc_conversation_id', models.CharField(max_length=255, unique=True, null=True)),
                ('email', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField()),
                ('prompt', models.ForeignKey(to='main.Prompt')),
                ('user', models.ForeignKey(to='main.User', null=True)),
            ],
        ),
    ]
