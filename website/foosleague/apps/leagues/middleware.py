from django.shortcuts import get_object_or_404
from django.http.response import HttpResponseRedirect
from django.conf import settings
import re
from leagues.models import League
subdomain_pattern = re.compile('(?P<subdomain>.*?)\..*?')

class SubdomainMiddleware(object):


    def process_request(self, request):

        # match = subdomain_pattern.match(request.get_host())
        # subdomain = match.group('subdomain')
        # if subdomain != 'foosleague' and subdomain != 'www':
        #     league = get_object_or_404(League.objects.filter(subdomain=subdomain))
        # else:
        #     # for now
        #     return HttpResponseRedirect('http://liftinteractive.foosleague.com/')
        # request.league = league
        request.league = None
        return
        # return request
