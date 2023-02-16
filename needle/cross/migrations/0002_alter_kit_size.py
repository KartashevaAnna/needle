# Generated by Django 4.1.5 on 2023-02-16 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cross", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="kit",
            name="size",
            field=models.IntegerField(
                blank=True,
                help_text="введите общее число крестиков в картине",
                null=True,
                verbose_name="size",
            ),
        ),
    ]
