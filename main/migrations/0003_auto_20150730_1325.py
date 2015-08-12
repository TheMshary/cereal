# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150730_1236'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cereal',
            old_name='shelf',
            new_name='display_shelf',
        ),
        migrations.AlterField(
            model_name='nutritionfacts',
            name='fiber',
            field=models.FloatField(null=True),
        ),
    ]
