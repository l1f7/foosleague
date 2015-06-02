from .models import Player


def player(request):
    if request.user.is_authenticated():
        try:
            player = Player.objects.get(user=request.user)
            return {'player': player}
        except:
            return {'player': ''}

