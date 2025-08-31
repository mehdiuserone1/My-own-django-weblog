from django.contrib import admin
from .models import Post, PostMedia



class PostMediaInline(admin.TabularInline):
    model = PostMedia
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug","author", "published", "created_at")
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("published", "created_at", "author")
    search_fields = ("title", "content")
    inlines = [PostMediaInline]


admin.site.register(PostMedia)
