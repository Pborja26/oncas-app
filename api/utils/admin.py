from django.contrib import admin
from django.utils.html import format_html
from utils import models

class BaseAuditModelAdmin(admin.ModelAdmin):
    readonly_fields = ("created_by", "created_at", "updated_by", "updated_at")

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by=request.user
        obj.updated_by=request.user


@admin.register(models.ThemeCategorie)
class ThemeCategoriesAdmin(BaseAuditModelAdmin):
    list_display = ("id", "name")
@admin.register(models.Theme)
class ThemeAdmin(BaseAuditModelAdmin):
    list_display = ("category__name", "name", "color", "color_preview", "active")
    list_filter = ["category__name"]

    @admin.display(description="Color", ordering="color")
    def color_preview(self, obj):
        return format_html(
            '<span style="display:inline-block;width:14px;height:14px;'
            'border:1px solid #999;border-radius:3px;vertical-align:middle;'
            'background:{};margin-right:6px"></span>{}',
            obj.color,
            obj.color,
        )
