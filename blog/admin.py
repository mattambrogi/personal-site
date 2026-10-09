from django import forms
from django.contrib import admin
from django.db import models
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "note", "show_in_feed", "format")
    prepopulated_fields = {"slug": ("title",)}
    fields = (
        "title",
        "author",
        "slug",
        "body_md",
        "body",
        "show_in_feed",
        "note",
    )
    # Give the Markdown field room to work in; the default admin textarea is
    # far too small to paste a full post into.
    formfield_overrides = {
        models.TextField: {"widget": forms.Textarea(attrs={"rows": 32, "cols": 100})},
    }

    @admin.display(description="Format")
    def format(self, obj):
        return "Markdown" if obj.body_md.strip() else "HTML (legacy)"
