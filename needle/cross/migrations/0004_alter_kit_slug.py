# Generated by Django 4.1.5 on 2023-01-28 15:17

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cross", "0003_kit_slug_alter_project_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="kit",
            name="slug",
            field=autoslug.fields.AutoSlugField(editable=False, populate_from="title"),
        ),
    ]
