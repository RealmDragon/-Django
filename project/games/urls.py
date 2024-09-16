from django.urls import path, include
from games.apps import GamesConfig
from games.views import GameListView, GameDetailView, GameCreateView, GameUpdateView, GameDeleteView

from project.games.views import GameDeleteView

games = GamesConfig.name

urlpatterns = [
    path('', GameListView.as_view(), name="games_list"),
    path('games/<int:pk>/', GameDetailView.as_view(), name="games_detail"),
    path('games/create', GameCreateView.as_view(), name="games_create"),
    path('games/<int:pk>/update', GameUpdateView.as_view(), name="games_update"),
    path('games/<int:pk>/delete/', GameDeleteView.as_view(), name="games_delete")

]