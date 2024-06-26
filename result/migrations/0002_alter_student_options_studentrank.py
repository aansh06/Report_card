# Generated by Django 5.0.4 on 2024-04-05 15:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("result", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="student",
            options={
                "ordering": ["student_id", "student_name"],
                "verbose_name": "student",
            },
        ),
        migrations.CreateModel(
            name="StudentRank",
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
                ("date_of_report_card_generation", models.DateField(auto_created=True)),
                ("student_rank", models.IntegerField()),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="studentreportcard",
                        to="result.student",
                    ),
                ),
            ],
        ),
    ]
