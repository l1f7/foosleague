import requests

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel
from django.core.urlresolvers import reverse_lazy

from teams.models import Team
from seasons.models import Season
from leagues.models import League
# from players.models import Player
from .utils import update_trueskill
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

    # def save(self):
    #     # todo: update denorm-ed streak counter
    #     pass

    # def delete(self):
    #     # todo: update denorm-ed streak counter
    #     pass
    def get_winning_percentage(self, team=1):
        from .utils import winning_percentage
        if team == 1:
            return winning_percentage(self, self.team_1)
        else:
            return winning_percentage(self, self.team_2)

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



        # send message
        if self.team_2_score == 0 or self.team_1_score == 0:
            message = ":skunk: :skunk: :skunk: *%s* _(%s)_ vs *%s* _(%s)_ :skunk: :skunk: :skunk: (http://%s.foosleague.com%s)" % (self.winner,
                                                                                                                                   winning_score, loser, losing_score, request.league.subdomain, self.get_absolute_url())
        else:
            message = "Game Over! *%s* _(%s)_ vs *%s* _(%s)_ (http://%s.foosleague.com%s)" % (self.winner,
                                                                                              winning_score, loser,  losing_score, request.league.subdomain, self.get_absolute_url())

        requests.post('https://liftinteractive.slack.com/services/hooks/slackbot?token=%s&channel=%s' % (request.league.slack_token, "%23" + request.league.slack_channel,),
                      data=message)


        # calculate streaks

        if self.winner == self.team_1:
            self.team_2.streak = 0
            self.team_1.streak += 1
            self.team_1.save()
            if self.team_1.streak > self.team_1.best_streak:
                self.team_1.best_streak = self.team_1.streak
                self.team_1.best_streak_date = datetime.now()

        else:
            self.team_1.streak = 0
            self.team_2.streak += 1

            if self.team_2.streak > self.team_2.best_streak:
                self.team_2.best_streak = self.team_2.streak
                self.team_2.best_streak_date = datetime.now()

        self.team_1.save()
        self.team_2.save()
        self.save()

        # recalculate trueskill
        update_trueskill(self)
