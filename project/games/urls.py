from django.urls import path, include
from games.apps import GamesConfig
from games.views import home

games = GamesConfig.name

urlpatterns = [
    path('', home, name='home')
]