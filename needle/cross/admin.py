from django.contrib import admin

from .models import Kit, Progress, Project, Designer, Company


class DesignerAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "name_translation",
        "slug",
        "country",
        "description",
    )


class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "name_translation",
        "slug",
        "country",
        "description",
    )


class KitAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "created",
        "description",
        "designer",
        "company",
        "creator",
        "size",
        "design_created_year",
        "design_created",
        "slug",
        "name_translation",
    )
    list_editable = (
        "designer",
        "company",
        "size",
        "design_created",
        "name_translation",
    )
    list_display_links = ("name",)
    search_fields = ("name", "designer", "company")


class ProjectAdmin(admin.ModelAdmin):
    def name(self, obj):
        return [kit.name for kit in obj.kit.all()]

    list_display = (
        "kit",
        "embroiderer",
        "slug",
        "description",
        "created",
        "name",
        "size",
    )
    search_fields = ("kit", "embroiderer")
    list_filter = ("kit", "embroiderer")


#
#
class ProgressAdmin(admin.ModelAdmin):
    fields = (
        "embroiderer",
        "project",
        "done",
        "remains",
        "name",
    )
    list_display = (
        "embroiderer",
        "project",
        "done",
        "remains",
        "name",
        "created",
        "pk",
    )
    list_editable = (
        "done",
        "project",
    )
    search_fields = ("project", "embroiderer")
    list_filter = ("project", "embroiderer")


admin.site.register(Designer, DesignerAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Kit, KitAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Progress, ProgressAdmin)
