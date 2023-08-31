# Generated by Django 4.2.4 on 2023-08-31 02:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_rename_first_name_users_name_remove_users_last_name"),
        ("leave", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="LeaveRequest",
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
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("reason", models.TextField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("approved", "Approved"),
                            ("rejected", "Rejected"),
                        ],
                        default="pending",
                        max_length=20,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="users.users"
                    ),
                ),
                (
                    "leave_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="leave.leavetype",
                    ),
                ),
            ],
        ),
    ]
