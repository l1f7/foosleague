from datetime import date
from .models import Season


def current_season(request):

    today = date.today()
    current_season = Season.objects.filter(league=request.league, start__lte=today, end__gte=today)
    try:
        season = current_season[0]
    except:
        season = None
    extra_context = {'season': season}
    return extra_context