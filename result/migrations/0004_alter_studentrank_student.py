# Generated by Django 5.0.4 on 2024-04-05 16:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("result", "0003_alter_studentrank_date_of_report_card_generation_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="studentrank",
            name="student",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="studentrank",
                to="result.student",
            ),
        ),
    ]
