from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['id', 'username', 'date_joined', 'is_active',]
    list_display_links = ['id', 'username',]
    fieldsets = [
        ("Profile", {
            "fields": ("username", "password", "name", "phone", "email",),
            "classes": ("wide",),
        },),
        ("Permissions", {
            "fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions",),
            "classes": ("collapse",),
        },),
        ("Important Dates", {
            "fields": ("last_login", "date_joined"),
            "classes": ("collapse",),
        },),
    ]

admin.site.register(User, CustomUserAdmin)
