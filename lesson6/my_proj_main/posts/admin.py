from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    # Настройка полей списка записи
    list_display = ['title', 'text', 'pub_date']
    # Фильтрация по дате публикации
    list_filter = ['pub_date']
    # Поисковая строка по конкретному значению
    search_fields = ['title', 'text']
    
    # Значение по умолчанию для пустого поля
    # empty_value_display = ['-Пусто-']
    # @admin.display(empty_value='-Пустое поле-')
    # def text(self, obj):
    #     return obj.text
    
    # Исклюючение отдельных полей записи
    #exclude = ['text']

    # Группировка полей
    fieldsets = (
        ('Главные', {
            'fields': ('title', 'text')
        }),
        ('Вторичные поля', {
            'classes': ['collapse'],
            'fields': ('author', )
        })
    )


admin.site.register(Post, PostAdmin)

