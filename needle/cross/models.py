from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class CreatedModel(models.Model):
    """Абстрактная модель. Добавляет дату создания."""

    created = models.DateTimeField(
        "Дата создания",
        auto_now_add=True,
        db_index=True,
    )

    class Meta:
        abstract = True


class CreatedUpdatedModel(CreatedModel):
    modified = models.DateTimeField(
        "Дата изменения",
        auto_now=True,
    )


class Kit(CreatedModel):
    title = models.TextField("Название картины", help_text="Введите название картины")
    description = models.TextField(null=True, blank=True)
    author = models.CharField("Автор", help_text="Введите автора картины")
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Создала набор на сайте",
        related_name="kit_created",
    )
    total_crosses = models.PositiveIntegerField(
        "размер картины", help_text="введите общее число крестиков в картине"
    )
    design_created_year = models.DateField(
        "Год создания дизайна",
        help_text="Введите год, в котором был разработан дизайн",
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ["-created"]
        unique_together = (
            "title",
            "author",
        )


class Project(CreatedModel):
    kit = models.ForeignKey(
        Kit, on_delete=models.CASCADE, verbose_name="Набор", related_name="kit"
    )
    embroiderer = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Набор", related_name="kit"
    )
    slug = models.SlugField(
        max_length=250,
        null=True,
        blank=True,
        unique=True,
    )
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class Progress(CreatedUpdatedModel):
    embroiderer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="progress",
        verbose_name="Прогресс",
    )
    kit = models.ForeignKey(
        Kit,
        on_delete=models.CASCADE,
        verbose_name="Картина",
        related_name="kit",
    )
    crosses_done = models.PositiveIntegerField(
        "Вышито крестиков", help_text="Введите количество вышитых крестиков"
    )

    class Meta:
        ordering = ["-modified"]
        verbose_name = ("прогресс",)
        unique_together = (
            "embroiderer",
            "kit",
        )


# Create your models here.
