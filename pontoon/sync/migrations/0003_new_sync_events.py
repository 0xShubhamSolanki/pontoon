# Generated by Django 4.2.17 on 2025-01-16 08:24

import django.db.models.deletion
import django.utils.timezone

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0071_alter_repository_type"),
        ("sync", "0002_change_pontoon_sync_email"),
    ]

    operations = [
        migrations.CreateModel(
            name="Sync",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.IntegerField(
                        choices=[
                            (0, "In Progress"),
                            (1, "Done"),
                            (2, "No Changes"),
                            (10, "No Commit"),
                            (20, "Prev Busy"),
                            (-1, "Fail"),
                            (-2, "Incomplete"),
                        ],
                        default=0,
                    ),
                ),
                ("start_time", models.DateTimeField(default=django.utils.timezone.now)),
                ("end_time", models.DateTimeField(blank=True, default=None, null=True)),
                ("error", models.TextField(default="")),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="base.project"
                    ),
                ),
            ],
        ),
    ]
