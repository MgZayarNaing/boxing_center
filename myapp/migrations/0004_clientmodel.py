# Generated by Django 4.2.1 on 2024-01-28 16:28

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0003_blogmodel"),
    ]

    operations = [
        migrations.CreateModel(
            name="ClientModel",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("img", models.ImageField(default=None, upload_to="")),
                ("title", models.CharField(blank=True, max_length=255, null=True)),
                ("contact", models.CharField(blank=True, max_length=255, null=True)),
                ("created_at", models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
