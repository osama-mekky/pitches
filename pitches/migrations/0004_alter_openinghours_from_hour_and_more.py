# Generated by Django 4.2.5 on 2023-11-23 05:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pitches', '0003_alter_openinghours_from_hour_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openinghours',
            name='from_hour',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 23, 8, 36, 4, 390983)),
        ),
        migrations.AlterField(
            model_name='openinghours',
            name='to_hour',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 23, 8, 36, 4, 390983)),
        ),
    ]
