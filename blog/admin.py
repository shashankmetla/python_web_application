from django.contrib import admin
from .models import Category, Post


@admin.register(Post)
class CustomPostAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at", "category", "written_by", "draft"]
    search_fields = ("title", "category", "written_by")
    list_filter = ("draft",)
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Category)
class CustomCategoryAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}
