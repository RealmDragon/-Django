from django.db import models
from django.utils.text import slugify

class Type(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название Жанра', help_text='Введите Название Жанра')
    description = models.TextField(verbose_name='Описание Жанра', help_text='Введите Описание Жанра')

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name

class Game(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название Игры', help_text='Введите Название Игры')
    type = models.ForeignKey(on_delete=models.SET_NULL, verbose_name='Жанр Игры', help_text='Введите Жанр Игры', null=True, blank=True, related_name='games', Type)
    logo = models.ImageField(upload_to='games/LogoBank', blank=True, null=True, verbose_name='Лого Игры', help_text='Загрузить Лого Игры' )
    release = models.DateField(blank=True, null=True, verbose_name='Дата выхода Игры', help_text='Введите дату выхода Игры')

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'
        ordering = ['type', 'name']

    def __str__(self):
        return self.name

