from django.contrib import admin

from blog.models import Category, Comment, Location, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'created_at',
                    'description', 'slug')
    list_editable = ('is_published',)
    list_filter = ('is_published',)
    search_fields = ('title', 'description')
    list_display_links = ('title',)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'created_at',)
    list_editable = ('is_published',)
    list_filter = ('is_published',)
    search_fields = ('name',)
    list_display_links = ('name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'location',
                    'pub_date', 'is_published', 'created_at')
    list_editable = ('is_published', 'category')
    list_filter = ('category', 'is_published', 'pub_date')
    search_fields = ('title', 'text', 'author__username')
    list_display_links = ('title',)



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'post', 'author', 'created_at',)
    search_fields = ('text', 'author__username', 'post__title')
    list_filter = ('created_at',)
    list_display_links = ('text',)


admin.site.empty_value_display = 'Не задано'
