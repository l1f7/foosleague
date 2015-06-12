from .models import Player


def player(request):
    try:
        player = Player.objects.get(user=request.user)

        return {'player': player}
    except:

        return {}

