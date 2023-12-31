# Generated by Django 4.1.5 on 2023-09-05 09:10

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('designs', '0002_alter_album_uuid_alter_design_publish_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('2546bd3f-eac0-4d49-84e0-3906dedab6f1'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='design',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 5, 12, 10, 54, 875974)),
        ),
        migrations.AlterField(
            model_name='design',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('55fa2969-1235-4a8a-b208-ef6d2627e288'), primary_key=True, serialize=False, unique=True),
        ),
    ]
