from deep_translator import GoogleTranslator
from django.contrib.auth import get_user_model
from django.db import models
from pytils.translit import slugify

User = get_user_model()
translator = GoogleTranslator(source="auto", target="en")


class CreatedModel(models.Model):
    """Абстрактная модель. Добавляет дату создания."""

    created = models.DateTimeField(
        "Дата создания",
        auto_now_add=True,
        db_index=True,
    )
    name = models.TextField("name", help_text="Введите имя", null=True, blank=True)
    name_translation = models.CharField(
        "name_translation",
        help_text="Введите перевод названия на английский или нажмите Enter",
        max_length=100,
        null=True,
        blank=True,
    )
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def get_translation(self):
        return translator.translate(self.name)

    def __str__(self):
        return self.name

    def make_slug(self):
        value = str(slugify(self.name_translation))
        return value.lower().replace("-", "_")

    def save(self, *args, **kwargs):
        if not self.name_translation:
            self.name_translation = self.get_translation()
            self.slug = self.make_slug()
        super(CreatedModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class CreatedUpdatedModel(CreatedModel):
    modified = models.DateTimeField(
        "modified",
        auto_now=True,
    )


class Designer(CreatedModel):
    name = models.TextField("name", help_text="Введите имя", unique=True)

    country = models.TextField(
        "country",
        help_text="Введите страну производства",
        null=True,
        blank=True,
    )


class Company(CreatedModel):
    name = models.TextField("name", help_text="Введите имя", unique=True)
    country = models.TextField(
        "country",
        help_text="Введите страну производства",
        null=True,
        blank=True,
    )
    description = models.TextField(null=True, blank=True)


class Kit(CreatedModel):
    name = models.TextField(
        "name",
        help_text="Введите имя",
        unique=True,
    )
    designer = models.ForeignKey(
        Designer,
        on_delete=models.CASCADE,
        verbose_name="designer",
        related_name="kit",
        null=True,
        blank=True,
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        verbose_name="company",
        related_name="kit",
        null=True,
        blank=True,
    )

    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="kit_created_by",
        related_name="kit_created_by",
    )
    size = models.PositiveIntegerField(
        "size",
        help_text="введите общее число крестиков в картине",
        null=True,
        blank=True,
    )
    design_created = models.DateField(
        "Год создания дизайна",
        help_text="Введите год, в котором был разработан дизайн",
        null=True,
        blank=True,
    )
    length = models.PositiveIntegerField(null=True, blank=True)
    height = models.PositiveIntegerField(null=True, blank=True)

    def design_created_year(self):
        try:
            return self.design_created.strftime("%Y")
        except AttributeError:
            return None

    def save(self, *args, **kwargs):
        if not self.name_translation:
            self.name_translation = self.get_translation()
            self.slug = self.make_slug()
        if not self.size:
            try:
                self.size = int(self.length) * int(self.height)
            except TypeError:
                pass
        super(Kit, self).save(*args, **kwargs)

    class Meta:
        ordering = ["-created"]
        unique_together = (
            "name",
            "designer",
        )


class Project(CreatedModel):
    kit = models.ForeignKey(
        Kit, on_delete=models.CASCADE, verbose_name="kit", related_name="project"
    )
    embroiderer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="embroiderer",
        related_name="project",
    )
    slug = models.SlugField(null=True, blank=True)

    def make_slug(self):
        value = str(slugify(self.embroiderer.get_full_name())) + "_" + self.kit.slug
        return value.lower().replace("-", "_")

    def size(self):
        size = self.kit.size
        return size

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.make_slug()
        if not self.name:
            self.name = self.slug
        super(Project, self).save(*args, **kwargs)

    description = models.TextField(null=True, blank=True)


class Progress(CreatedModel):
    embroiderer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="progress",
        verbose_name="пользователь",
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        verbose_name="project",
        related_name="progress",
    )

    done = models.PositiveIntegerField(
        "done",
        help_text="Введите количество вышитых крестиков",
    )
    created = models.DateTimeField(
        "created",
        auto_now=True,
    )
    modified = models.DateTimeField(
        "modified",
        auto_now=True,
    )
    remains = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    def get_remaining_crosses(self):
        self.remains = self.project.kit.size - self.done

    def get_name(self):
        name = str(self.project.name)
        return name

    def save(self, *args, **kwargs):
        self.get_remaining_crosses()
        if not self.name:
            self.name = self.get_name()
        super(Progress, self).save(*args, **kwargs)

    class Meta:
        ordering = ["-modified"]
        unique_together = ("embroiderer", "project", "modified")
