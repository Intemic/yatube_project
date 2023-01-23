from django.contrib import admin
from .models import Group, Post


class GroupAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'description',
    )
    search_fields = ('title',)


class PostAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = (
        'text',
        'pub_date',
        'author',
        'group',
    )
    list_editable = ('group',)
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('text', )
    # Добавляем возможность фильтрации по дате
    list_filter = ('pub_date',)


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)