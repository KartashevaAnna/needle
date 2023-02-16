# Generated by Django 4.1.5 on 2023-02-16 09:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Company",
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
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, db_index=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "name_translation",
                    models.CharField(
                        blank=True,
                        help_text="Введите перевод названия на английский или нажмите Enter",
                        max_length=100,
                        null=True,
                        verbose_name="name_translation",
                    ),
                ),
                ("slug", models.SlugField(blank=True, null=True)),
                (
                    "name",
                    models.TextField(
                        help_text="Введите имя", unique=True, verbose_name="name"
                    ),
                ),
                (
                    "country",
                    models.TextField(
                        blank=True,
                        help_text="Введите страну производства",
                        null=True,
                        verbose_name="country",
                    ),
                ),
                ("description", models.TextField(blank=True, null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="CreatedUpdatedModel",
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
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, db_index=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "name",
                    models.TextField(
                        blank=True,
                        help_text="Введите имя",
                        null=True,
                        verbose_name="name",
                    ),
                ),
                (
                    "name_translation",
                    models.CharField(
                        blank=True,
                        help_text="Введите перевод названия на английский или нажмите Enter",
                        max_length=100,
                        null=True,
                        verbose_name="name_translation",
                    ),
                ),
                ("slug", models.SlugField(blank=True, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "modified",
                    models.DateTimeField(auto_now=True, verbose_name="modified"),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Designer",
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
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, db_index=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "name_translation",
                    models.CharField(
                        blank=True,
                        help_text="Введите перевод названия на английский или нажмите Enter",
                        max_length=100,
                        null=True,
                        verbose_name="name_translation",
                    ),
                ),
                ("slug", models.SlugField(blank=True, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "name",
                    models.TextField(
                        help_text="Введите имя", unique=True, verbose_name="name"
                    ),
                ),
                (
                    "country",
                    models.TextField(
                        blank=True,
                        help_text="Введите страну производства",
                        null=True,
                        verbose_name="country",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Kit",
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
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, db_index=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "name_translation",
                    models.CharField(
                        blank=True,
                        help_text="Введите перевод названия на английский или нажмите Enter",
                        max_length=100,
                        null=True,
                        verbose_name="name_translation",
                    ),
                ),
                ("slug", models.SlugField(blank=True, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "name",
                    models.TextField(
                        help_text="Введите имя", unique=True, verbose_name="name"
                    ),
                ),
                (
                    "size",
                    models.PositiveIntegerField(
                        blank=True,
                        help_text="введите общее число крестиков в картине",
                        null=True,
                        verbose_name="size",
                    ),
                ),
                (
                    "design_created",
                    models.DateField(
                        blank=True,
                        help_text="Введите год, в котором был разработан дизайн",
                        null=True,
                        verbose_name="Год создания дизайна",
                    ),
                ),
                ("length", models.IntegerField(blank=True, null=True)),
                ("height", models.IntegerField(blank=True, null=True)),
                (
                    "company",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="kit",
                        to="cross.company",
                        verbose_name="company",
                    ),
                ),
                (
                    "creator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="kit_created_by",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="kit_created_by",
                    ),
                ),
                (
                    "designer",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="kit",
                        to="cross.designer",
                        verbose_name="designer",
                    ),
                ),
            ],
            options={
                "ordering": ["-created"],
                "unique_together": {("name", "designer")},
            },
        ),
        migrations.CreateModel(
            name="Project",
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
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, db_index=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "name",
                    models.TextField(
                        blank=True,
                        help_text="Введите имя",
                        null=True,
                        verbose_name="name",
                    ),
                ),
                (
                    "name_translation",
                    models.CharField(
                        blank=True,
                        help_text="Введите перевод названия на английский или нажмите Enter",
                        max_length=100,
                        null=True,
                        verbose_name="name_translation",
                    ),
                ),
                ("slug", models.SlugField(blank=True, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "embroiderer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="project",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="embroiderer",
                    ),
                ),
                (
                    "kit",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="project",
                        to="cross.kit",
                        verbose_name="kit",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Progress",
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
                (
                    "name",
                    models.TextField(
                        blank=True,
                        help_text="Введите имя",
                        null=True,
                        verbose_name="name",
                    ),
                ),
                (
                    "name_translation",
                    models.CharField(
                        blank=True,
                        help_text="Введите перевод названия на английский или нажмите Enter",
                        max_length=100,
                        null=True,
                        verbose_name="name_translation",
                    ),
                ),
                ("slug", models.SlugField(blank=True, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "done",
                    models.PositiveIntegerField(
                        help_text="Введите количество вышитых крестиков",
                        verbose_name="done",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now=True, verbose_name="created"),
                ),
                (
                    "modified",
                    models.DateTimeField(auto_now=True, verbose_name="modified"),
                ),
                ("remains", models.PositiveIntegerField(blank=True, null=True)),
                (
                    "embroiderer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="progress",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="пользователь",
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="progress",
                        to="cross.project",
                        verbose_name="project",
                    ),
                ),
            ],
            options={
                "ordering": ["-modified"],
                "unique_together": {("embroiderer", "project", "modified")},
            },
        ),
    ]
