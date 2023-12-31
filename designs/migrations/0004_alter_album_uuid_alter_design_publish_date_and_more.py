# Generated by Django 4.1.5 on 2023-09-05 09:11

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('designs', '0003_alter_album_uuid_alter_design_publish_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('7ddc2d5a-0097-471f-b207-4c650864c104'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='design',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 5, 12, 11, 8, 213128)),
        ),
        migrations.AlterField(
            model_name='design',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('7c07ee36-d0e1-46c2-9736-7f3879f9e6a8'), primary_key=True, serialize=False, unique=True),
        ),
    ]
