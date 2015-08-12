# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20150730_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nutritionfacts',
            name='carbs',
            field=models.FloatField(null=True),
        ),
    ]
