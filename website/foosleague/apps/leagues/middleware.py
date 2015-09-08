from django.shortcuts import get_object_or_404
from django.http.response import HttpResponseRedirect
from django.conf import settings
import re
from leagues.models import League, LeagueMember
from seasons.models import Season
from players.models import Player
subdomain_pattern = re.compile('(?P<subdomain>.*?)\..*?')

from datetime import datetime

class SubdomainMiddleware(object):

    def process_request(self, request):
        match = subdomain_pattern.match(request.get_host())
        subdomain = match.group('subdomain')


        if subdomain != 'foosleague' and subdomain != 'www':
            league = get_object_or_404(League.objects.filter(subdomain=subdomain))
            # try:
            #     lm = LeagueMember.objects.get(league=league)
            # except:
            #     return HttpResponseRedirect('http://foosleague.com/tease/')


        else:
            # for now
            return HttpResponseRedirect('http://liftinteractive.foosleague.com/matches/')

        if request.user.is_authenticated():
            #make sure user is apart of league
            player = Player.objects.get(user=request.user)
            if player:
                request.player = player

        try:
            request.season = Season.objects.get(id=request.session['season'])
        except:
            today = datetime.today()
            request.season = Season.objects.filter(start__lte=today, end__gte=today)[0]
            request.session['season'] = request.season.id

        request.league = league


        # else:
        #     request.league = None
        #     if request.user:
        #         player = Player.objects.filter(user=request.user)
        #         if player:
        #             request.player = player[0]
        return
        # return request
