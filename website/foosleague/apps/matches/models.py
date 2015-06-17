import requests

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel
from django.core.urlresolvers import reverse_lazy

from teams.models import Team
from seasons.models import Season
from leagues.models import League
# from players.models import Player
from .utils import update_trueskill, award_season_points, regen_expose, award_fooscoin, recalculate_streaks, broadcast_message
from datetime import datetime


class Match(TimeStampedModel):
    team_1 = models.ForeignKey(Team, related_name='team_1')
    team_2 = models.ForeignKey(Team, related_name='team_2')

    team_1_score = models.IntegerField(_("Team 1 Score"), default=0)
    team_2_score = models.IntegerField(_("Team 2 Score"), default=0)

    completed = models.BooleanField(_("Completed"), default=False)
    winner = models.ForeignKey(Team, related_name='winner', blank=True, null=True)

    season = models.ForeignKey(Season, verbose_name=_("Season"), blank=True, null=True)
    league = models.ForeignKey(League, verbose_name=_("League"))

    # points_awarded_team_1 = models.FloatField(_("Team 1 points"), default=0)
    # points_awarded_team_2 = models.FloatField(_("Team 2 points"), default=0)

    class Meta:
        verbose_name = _("Match")
        verbose_name_plural = _("Matches")
        ordering = ('-created',)

    def __unicode__(self):
        return '%s vs %s ' % (self.team_1, self.team_2,)

    def get_absolute_url(self):
        return reverse_lazy('match-detail', kwargs={'pk': self.id})


    def get_winning_percentage(self, team_number=1):
        from .utils import winning_percentage
        return winning_percentage(self, team_number)

    def complete(self, request):

        if self.team_1_score > self.team_2_score:
            self.winner = self.team_1
            loser = self.team_2
            winning_score = self.team_1_score
            losing_score = self.team_2_score
        elif self.team_2_score > self.team_1_score:
            self.winner = self.team_2
            loser = self.team_1
            winning_score = self.team_2_score
            losing_score = self.team_1_score

        self.save()


        # send message



        # calculate streaks
        broadcast_message(self, winning_score, losing_score, loser, request)
        recalculate_streaks(self)
        # recalculate trueskill
        update_trueskill(self)
        award_fooscoin(self)
        #award_season_points(self)
        regen_expose(self)