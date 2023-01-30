# Generated by Django 4.1.5 on 2023-01-30 10:39

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cross", "0007_kit_title_translation"),
    ]

    operations = [
        migrations.AlterField(
            model_name="kit",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                blank=True, editable=False, null=True, populate_from="title_translation"
            ),
        ),
        migrations.AlterField(
            model_name="kit",
            name="total_crosses",
            field=models.PositiveIntegerField(
                blank=True,
                help_text="введите общее число крестиков в картине",
                null=True,
                verbose_name="размер картины",
            ),
        ),
    ]