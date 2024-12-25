from django.contrib import admin
from .models import Car, Comment


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'image')
    search_fields = ('brand', 'model')
    list_filter = ('year',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('car', 'user', 'text', 'created_at')
    search_fields = ('text', 'user__username', 'car__brand', 'car__model')
    list_filter = ('created_at', 'user', 'car')
