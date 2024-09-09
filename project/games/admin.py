from django.contrib import admin
from .models import Game, Type

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type')  # Изменено
    list_filter = ('type',)
    search_fields = ('name',)


@admin.register(Type)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Изменено

