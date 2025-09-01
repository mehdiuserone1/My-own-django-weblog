from django.contrib import admin
from .models import Post, PostMedia, Tag



class PostMediaInline(admin.TabularInline):
    model = PostMedia
    extra = 1


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ["name"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug","author", "published", "created_at")
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("published", "created_at", "author", "tags")
    search_fields = ("title", "content")
    filter_horizontal = ("tags",)
    inlines = [PostMediaInline]


admin.site.register(PostMedia)
