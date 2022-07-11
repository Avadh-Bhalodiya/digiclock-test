# Generated by Django 3.1.7 on 2022-07-09 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("core", "0001_initial"), ("employee", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="EmployeeConfig",
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
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("is_deleted", models.BooleanField(db_index=True, default=False)),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="core.userprofile",
                    ),
                ),
                (
                    "work_config",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="employee.workconfig",
                    ),
                ),
            ],
            options={"abstract": False},
        )
    ]
