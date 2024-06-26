# Generated by Django 5.0.4 on 2024-04-05 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("result", "0002_alter_student_options_studentrank"),
    ]

    operations = [
        migrations.AlterField(
            model_name="studentrank",
            name="date_of_report_card_generation",
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterUniqueTogether(
            name="studentrank",
            unique_together={("student_rank", "date_of_report_card_generation")},
        ),
    ]
