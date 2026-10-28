from django.contrib import admin

class BaseAuditModelAdmin(admin.ModelAdmin):
    readonly_fields = ("created_by", "created_at", "updated_by", "updated_at")

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by=request.user
        obj.updated_by=request.user
