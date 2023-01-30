from django.contrib import admin

from .models import Kit, Progress, Project, Designer, Company


class DesignerAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "title_translation",
        "slug",
        "country",
        "description",
    )


class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "title_translation",
        "slug",
        "country",
        "description",
        "designer",
    )


class KitAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "created",
        "description",
        "designer",
        "company",
        "creator",
        "total_crosses",
        "design_created_year",
        "slug",
        "title_translation",
    )
    search_fields = ("title", "designer", "company")


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
admin.site.register(Designer, DesignerAdmin)
admin.site.register(Company, CompanyAdmin)
