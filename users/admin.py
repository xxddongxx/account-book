from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = [
        "id",
        "email",
        "username",
        "date_joined",
        "is_active",
    ]
    list_display_links = [
        "id",
        "email",
        "username",
    ]
    fieldsets = [
        (
            "Profile",
            {
                "fields": (
                    "email",
                    "password",
                    "username",
                    "phone",
                ),
                "classes": ("wide",),
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
                "classes": ("collapse",),
            },
        ),
        (
            "Important Dates",
            {
                "fields": ("last_login", "date_joined"),
                "classes": ("collapse",),
            },
        ),
    ]


admin.site.register(User, CustomUserAdmin)
