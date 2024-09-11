from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from games.models import Game

class GameListView(ListView):
    model = Game

class GameDetailView(DetailView):
    model = Game

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views.counter += 1
        self.object.save()
        return self.object

class GameCreateView(CreateView):
    model = Game
    fields = ('name', 'type', 'release_date', 'logo')
    success_url = reverse_lazy('games:games_list')

class GameUpdateView(UpdateView):
    model = Game
    fields = ('name', 'type', 'release_date', 'logo')
    success_url = reverse_lazy('games:games_list')

    def get_success_url(self):
        return reverse('games:games_detail', args=[self.object.kwargs.get('pk')])
class GameDeleteView(DeleteView):
    model = Game
    success_url = reverse_lazy('games:games_list')