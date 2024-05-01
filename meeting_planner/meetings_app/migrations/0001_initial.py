# Generated by Django 5.0.2 on 2024-05-01 16:13

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Room",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("room_name", models.CharField(max_length=200)),
                ("floor_number", models.IntegerField()),
                ("room_number", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Meeting",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=150)),
                ("date", models.DateField()),
                ("start_time", models.TimeField(default=datetime.time(9, 0))),
                ("duration", models.IntegerField(default=1)),
                (
                    "room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="meetings_app.room",
                    ),
                ),
            ],
        ),
    ]