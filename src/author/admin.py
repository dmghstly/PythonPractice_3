"""
Функции панели управления для приложения "Выполненные работы".
"""

from django.contrib import admin

from author.models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "resume_ref",
        "github_ref",
        "email",
        "created_at",
        "updated_at",
    )

    search_fields = ("email",)

    list_filter = (
        "created_at",
        "updated_at",
    )
