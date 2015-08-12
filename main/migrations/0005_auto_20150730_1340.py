# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20150730_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cereal',
            name='ss_weight',
            field=models.FloatField(null=True),
        ),
    ]
