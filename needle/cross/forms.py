from django import forms

from .models import Kit, Progress, Project


class KitForm(forms.ModelForm):
    class Meta:
        model = Kit
        fields = (
            "title",
            "description",
            "author",
            "total_crosses",
            "creator",
            "total_crosses",
            "design_created_year",
        )
        labels = {
            "title": "Название картины",
            "description": "Описание картины",
            "author": "Имя дизайнера",
            "total_crosses": "Всего крестиков",
            "design_created_year": "Год создания дизайна",
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ("kit", "embroiderer", "slug", "description")
        labels = {
            "kit": "дизайн",
            "embroiderer": "вышивальщица",
            "slug": "слаг",
            "description": "описание",
        }


class ProgressForm(forms.ModelForm):
    class Meta:
        model = Progress
        fields = (
            "embroiderer",
            "kit",
            "crosses_done",
        )
        labels = {
            "embroiderer": "вышивальщица",
            "kit": "набор",
            "crosses_done": "Вышито крестиков",
        }
        help_texts = {
            "text-help": "Введите количество вышитых крестиков",
        }
