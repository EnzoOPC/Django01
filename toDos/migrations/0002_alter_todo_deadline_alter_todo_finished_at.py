# Generated by Django 5.1.2 on 2024-10-14 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("toDos", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="deadline",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="todo",
            name="finished_at",
            field=models.DateField(null=True),
        ),
    ]
