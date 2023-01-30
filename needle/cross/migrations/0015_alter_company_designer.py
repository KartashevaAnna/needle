# Generated by Django 4.1.5 on 2023-01-30 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("cross", "0014_company"),
    ]

    operations = [
        migrations.AlterField(
            model_name="company",
            name="designer",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="designer",
                to="cross.designer",
                verbose_name="Дизайнер",
            ),
        ),
    ]
