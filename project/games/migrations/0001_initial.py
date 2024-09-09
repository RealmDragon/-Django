import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Type",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Введите название Жанра",
                        max_length=100,
                        verbose_name="Название Жанра",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Введите описание Жанра",
                        null=True,
                        verbose_name="Описание Жанра",
                    ),
                ),
            ],
            options={
                "verbose_name": "Жанр",
                "verbose_name_plural": "Жанры",
            },
        ),
        migrations.CreateModel(
            name="Game",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Введите название игры",
                        max_length=100,
                        verbose_name="Название Игры",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        help_text="Введите описание игры",
                        verbose_name="Описание игры",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите лого игры",
                        null=True,
                        upload_to="games/LogoBank",
                        verbose_name="лого игры",
                    ),
                ),
                (
                    "price",
                    models.IntegerField(
                        help_text="цена игры",
                        verbose_name="Цена за покупку игры",
                    ),
                ),
                (
                    "created_at",
                    models.DateField(
                        blank=True,
                        help_text="Укажите дату выпуска",
                        null=True,
                        verbose_name="Дата выпуска",
                    ),
                ),
                (
                    "updated_at",
                    models.DateField(
                        blank=True,
                        help_text="Укажите дату последнего изменения",
                        null=True,
                        verbose_name="Дата последнего изменения",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        help_text="Введите название жанра игры",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="games",
                        to="games.type",
                        verbose_name="жанр игры",
                    ),
                ),
            ],
            options={
                "verbose_name": "Игра",
                "verbose_name_plural": "Игры",
                "ordering": ["type", "name"],
            },
        ),
    ]