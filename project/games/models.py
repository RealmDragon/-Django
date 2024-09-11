from django.db import models

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
    type = models.ForeignKey(on_delete=models.SET_NULL, verbose_name='Жанр Игры', help_text='Введите Жанр Игры', null=True, blank=True, related_name='games_media', Type)
    logo = models.ImageField(upload_to='games_media/LogoBank', blank=True, null=True, verbose_name='Лого Игры', help_text='Загрузить Лого Игры' )
    release = models.DateField(blank=True, null=True, verbose_name='Дата выхода Игры', help_text='Введите дату выхода Игры')
    view_counter = models.PositiveIntegerField(default=0, verbose_name='Счетик просмотров', help_text='Просмотры', default=0)

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'
        ordering = ['type', 'name']

    def __str__(self):
        return self.name

