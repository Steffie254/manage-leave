# Generated by Django 4.2.4 on 2023-08-29 15:43

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Users",
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
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("gender", models.BinaryField(max_length=100)),
                ("department", models.CharField(max_length=100)),
                ("phone_number", models.IntegerField(null=True)),
                ("email_address", models.TextField(blank=True, null=True)),
            ],
        ),
    ]