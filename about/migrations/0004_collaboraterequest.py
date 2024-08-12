# Generated by Django 4.2.14 on 2024-08-12 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("about", "0003_rename_text_about_context"),
    ]

    operations = [
        migrations.CreateModel(
            name="CollaborateRequest",
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
                ("name", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=254)),
                ("message", models.TextField()),
                ("read", models.BooleanField(default=False)),
            ],
        ),
    ]