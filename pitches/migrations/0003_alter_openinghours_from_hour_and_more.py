# Generated by Django 4.2.5 on 2023-11-13 00:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pitches', '0002_alter_openinghours_from_hour_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openinghours',
            name='from_hour',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 13, 3, 3, 16, 429176)),
        ),
        migrations.AlterField(
            model_name='openinghours',
            name='to_hour',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 13, 3, 3, 16, 429176)),
        ),
    ]
