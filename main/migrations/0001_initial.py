# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cereal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=30)),
                ('cereal_type', models.CharField(max_length=1, null=True)),
                ('ss_weight', models.IntegerField(null=True)),
                ('cps', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DisplayShelf',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='NutritionFacts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('calories', models.IntegerField(null=True)),
                ('protein', models.IntegerField(null=True)),
                ('fat', models.IntegerField(null=True)),
                ('fiber', models.IntegerField(null=True)),
                ('carbs', models.IntegerField(null=True)),
                ('sugar', models.IntegerField(null=True)),
                ('sodium', models.IntegerField(null=True)),
                ('potassium', models.IntegerField(null=True)),
                ('vitamins_minerals', models.IntegerField(null=True)),
                ('cereal', models.OneToOneField(to='main.Cereal')),
            ],
        ),
        migrations.AddField(
            model_name='cereal',
            name='display_shelf',
            field=models.ForeignKey(to='main.DisplayShelf'),
        ),
        migrations.AddField(
            model_name='cereal',
            name='manufacturer',
            field=models.ForeignKey(to='main.Manufacturer', null=True),
        ),
    ]
