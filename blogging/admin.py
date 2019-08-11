from django.contrib import admin
from blogging.models import Post, Category


class CategoryInline(admin.StackedInline):
    model = Category.posts.through


class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline,
    ]
    fields = ('title', 'body', 'author', 'published_date')
    list_display = ('title', 'author', 'created_date')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    exclude = ('posts',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)