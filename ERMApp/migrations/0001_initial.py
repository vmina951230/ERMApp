# Generated by Django 4.1.7 on 2023-02-23 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Position",
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
                ("title", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Employee",
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
                ("empid", models.CharField(max_length=10)),
                ("empname", models.CharField(max_length=100)),
                ("designation", models.CharField(max_length=20)),
                (
                    "Position",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ERMApp.position",
                    ),
                ),
            ],
        ),
    ]
