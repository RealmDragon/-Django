from django.shortcuts import render, get_object_or_404

from games.models import Game
def games_list(request):
    games = Game.objects.all()
    context = {'games': games}
    return render(request, 'games_list.html', context)

def dogs_detail(request, pk):
    game = get_object_or_404(Game, pk=)
    context = {'games': game}
    return render(request, 'dogs_detail.html', context)



