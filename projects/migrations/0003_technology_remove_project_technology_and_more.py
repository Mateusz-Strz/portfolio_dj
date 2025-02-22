# Generated by Django 5.1.3 on 2025-01-29 20:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0002_project_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Technology",
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
                ("name", models.CharField(max_length=100)),
                ("icon", models.ImageField(upload_to="technologies")),
            ],
        ),
        migrations.RemoveField(
            model_name="project",
            name="technology",
        ),
        migrations.AddField(
            model_name="project",
            name="technologies",
            field=models.ManyToManyField(to="projects.technology"),
        ),
    ]
