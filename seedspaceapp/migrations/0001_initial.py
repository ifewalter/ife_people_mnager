# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('full_name', models.TextField(max_length=100)),
                ('email_address', models.EmailField(max_length=254)),
            ],
        ),
    ]
