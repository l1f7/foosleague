from .models import League


def leagues(request):
    try:
        leagues = League.objects.filter(player__user=request.user)

        return {'leagues': leagues}
    except:

        return {}

