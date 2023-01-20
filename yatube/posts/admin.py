from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('text', 'pub_date', 'author')
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('text', )
    # Добавляем возможность фильтрации по дате
    list_filter = ('pub_date',)


# Register your models here.
admin.site.register(Post, PostAdmin)
