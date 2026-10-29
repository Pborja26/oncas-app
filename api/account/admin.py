from django.contrib import admin
from account import models

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username")
    readonly_fields = ("last_login", "date_joined")
    filter_horizontal = ("groups", "user_permissions")
    list_filter = ["groups"]
    search_fields = ["id", "first_name", "last_name", "email", "username"]
