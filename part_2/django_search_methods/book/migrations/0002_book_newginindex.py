# Generated by Django 4.0.2 on 2022-02-14 13:48

import django.contrib.postgres.indexes
from django.db import migrations
from django.contrib.postgres.operations import BtreeGinExtension


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        BtreeGinExtension(),
        migrations.AddIndex(
            model_name='book',
            index=django.contrib.postgres.indexes.GinIndex(fields=['title'], name='NewGinIndex'),
        ),
    ]
