# Generated by Django 4.1.5 on 2023-02-10 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cross", "0018_remove_designer_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="company",
            name="title",
            field=models.TextField(
                help_text="Введите имя", unique=True, verbose_name="Имя"
            ),
        ),
        migrations.AlterField(
            model_name="createdupdatedmodel",
            name="title",
            field=models.TextField(
                help_text="Введите имя", unique=True, verbose_name="Имя"
            ),
        ),
        migrations.AlterField(
            model_name="designer",
            name="title",
            field=models.TextField(
                help_text="Введите имя", unique=True, verbose_name="Имя"
            ),
        ),
        migrations.AlterField(
            model_name="kit",
            name="title",
            field=models.TextField(
                help_text="Введите имя", unique=True, verbose_name="Имя"
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="title",
            field=models.TextField(
                help_text="Введите имя", unique=True, verbose_name="Имя"
            ),
        ),
    ]
