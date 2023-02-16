from django import forms
from django.core.exceptions import ValidationError
from deep_translator import GoogleTranslator


from .models import Kit, Progress, Project

translator = GoogleTranslator(source="auto", target="en")


class KitForm(forms.ModelForm):
    class Meta:
        model = Kit
        fields = (
            "name",
            "name_translation",
            "description",
            "designer",
            "company",
            "size",
            "design_created",
            "length",
            "height",
        )
        labels = {
            "design_created": "Год создания дизайна",
        }
        help_texts = {
            "design_created": "Введите год в формате 2023-02-03 (год-месяц-день)",
        }

    def clean_name_translation(self):
        cleaned_data = super().clean()
        name_translation = cleaned_data.get("name_translation")
        if not name_translation:
            name = cleaned_data.get("name")
            name_translation = translator.translate(cleaned_data.get("name"))
        if Kit.objects.filter(name_translation=name_translation).exists():
            raise ValidationError(
                f'Перевод "{name_translation}" уже существует, '
                "придумайте уникальное значение"
            )
        return name_translation
