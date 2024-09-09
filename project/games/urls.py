from django.urls import path, include
from games.apps import GamesConfig
from games.view import game_list, game_detail

games = GamesConfig.name

urlpatterns = [
    path('', game_list, name="games_list"),
    path('games/<int:pk>/', game_detail, name="games_detail")

]