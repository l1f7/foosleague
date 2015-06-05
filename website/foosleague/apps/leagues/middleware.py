from django.shortcuts import get_object_or_404

import re
from leagues.models import League
subdomain_pattern = re.compile('(?P<subdomain>.*?)\..*?')

class SubdomainMiddleware(object):


    def process_request(self, request):

        match = subdomain_pattern.match(request.get_host())
        subdomain = match.group('subdomain')

        league = get_object_or_404(League.objects.filter(subdomain=subdomain))
        request.league = league

        print request.league

        return
        # return request
