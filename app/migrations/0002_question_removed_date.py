# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='removed_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 13, 4, 8, 46, 997323, tzinfo=utc), verbose_name=b'date removed'),
            preserve_default=False,
        ),
    ]
