from django.contrib import admin
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
    list_display = ("category__name", "name", "color", "active")
    list_filter = ["category__name"]