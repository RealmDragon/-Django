from django.urls import path, include
from games.apps import GamesConfig
from games.view import games_list, games

games = GamesConfig.name

urlpatterns = [
    path('', game_list, name="games_list"),
    path('games_media/<int:pk>/', game_detail, name="games_detail")

]