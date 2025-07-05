from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'isbn')
    list_filter = ('language',)
    search_fields = ('title', 'author', 'isbn')
    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'author')
        }),
        ('Details', {
            'fields': ('published_date', 'isbn', 'page_count'),
        }),
        ('Additional', {
            'fields': ('cover_url', 'language'),
            'classes': ('collapse',)
        }),
    )