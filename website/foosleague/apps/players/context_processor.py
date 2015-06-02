from .models import Player


def player(request):
    player = Player.objects.get(user=request.user)
    return {'player': player}
