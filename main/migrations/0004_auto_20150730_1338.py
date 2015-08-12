# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20150730_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cereal',
            name='display_shelf',
            field=models.ForeignKey(to='main.DisplayShelf', null=True),
        ),
    ]
