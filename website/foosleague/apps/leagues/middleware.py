from django.shortcuts import get_object_or_404
from django.http.response import HttpResponseRedirect
from django.conf import settings
import re
from leagues.models import League
from players.models import Player
subdomain_pattern = re.compile('(?P<subdomain>.*?)\..*?')


class SubdomainMiddleware(object):

    def process_request(self, request):
        if settings.DEBUG:
            match = subdomain_pattern.match(request.get_host())
            subdomain = match.group('subdomain')
            if subdomain != 'foosleague' and subdomain != 'www':
                league = get_object_or_404(League.objects.filter(subdomain=subdomain))
            else:
                # for now
                return HttpResponseRedirect('http://liftinteractive.foosleague.com/matches/')
            request.league = league
            if request.user:
                player = Player.objects.filter(user=request.user)
                if player:
                    request.player = player[0]

        else:
            request.league = None
            if request.user:
                player = Player.objects.filter(user=request.user)
                if player:
                    request.player = player[0]
        return
        # return request
