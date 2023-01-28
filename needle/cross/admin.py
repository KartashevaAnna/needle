from django.contrib import admin

from .models import Kit, Project, Progress


class KitAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "created",
        "description",
        "author",
        "creator",
        "total_crosses",
        "design_created_year",
    )
    search_fields = ("title", "author")
    list_filter = ("created", "autor")


class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "kit",
        "embroiderer",
        "slug",
        "description",
        "created",
    )
    search_fields = ("kit", "embroiderer")
    list_filter = ("kit", "embroiderer")


class ProgressAdmin(admin.ModelAdmin):
    list_display = (
        "embroiderer",
        "kit",
        "crosses_done",
        "created",
        "modified",
    )
    search_fields = ("kit", "embroiderer")
    list_filter = ("kit", "embroiderer")


admin.site.register(Kit, KitAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Progress, ProgressAdmin)
