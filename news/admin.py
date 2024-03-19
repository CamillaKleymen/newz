from django.contrib import admin
from .models import CategoryModel, NewsModel

@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_title', 'created_at']
    search_fields = ['category_title']
    list_filter = ['created_at']
    ordering = ['category_title']

@admin.register(NewsModel)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['pk', 'news_title', 'news_description', 'news_created_at']
    search_fields = ['news_title']
    list_filter = ['news_created_at']
    ordering = ['news_title']
