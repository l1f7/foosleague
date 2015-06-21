import requests
import json
from django.db import models
from django.db.models import Sum
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel
from django.core.urlresolvers import reverse_lazy

from teams.models import Team
from seasons.models import Season
from leagues.models import League
# from players.models import Player
from .utils import update_trueskill, award_season_points, regen_expose, award_fooscoin, recalculate_streaks, broadcast_message, shame_check
from datetime import datetime


class Match(TimeStampedModel):
    team_1 = models.ForeignKey(Team, related_name='team_1')
    team_2 = models.ForeignKey(Team, related_name='team_2')

    team_1_score = models.IntegerField(_("Team 1 Score"), default=0)
    team_2_score = models.IntegerField(_("Team 2 Score"), default=0)

    completed = models.BooleanField(_("Completed"), default=False)
    completed_date = models.DateTimeField(_("Completed Date"), blank=True,null=True)
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

    def team_1_wp(self):
        from .utils import winning_percentage
        return winning_percentage(self, 1)

    def team_2_wp(self):
        from .utils import winning_percentage
        return winning_percentage(self, 2)

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
        self.completed = True
        self.completed_date = datetime.now()
        self.save()

        # calculate streaks
        broadcast_message(self, winning_score, losing_score, loser, request)
        recalculate_streaks(self)
        # recalculate trueskill
        update_trueskill(self)
        award_fooscoin(self)
        shame_check(self, request)
        #award_season_points(self)
        regen_expose(self)

    @property
    def momentum(self):
        goals = self.goal_set.filter(value=1).order_by('created')

        ppm = 0.75
        ppg = 10

        momentum = []
        momentum_count=0
        team1_streak = 0
        team2_streak = 0
        team_1_score = 0
        team_2_score = 0
        last_goal_date = None
        count = 0

        for g in goals:
            duration_time = g.created - self.created
            d = divmod(duration_time.days * 86400 + duration_time.seconds, 60)
            duration = '%s:%s' % (d[0], str(d[1]).ljust(2,'0'))


            if last_goal_date is None:
                diff = (g.created - self.created).seconds/15
                for mins in range(0, int(round(diff))):
                    momentum.append([count, 0, None, None, 0, None, None])
                    count += 1
            else:
                #calculate minutes past
                diff = (g.created - last_goal_date).seconds/15
                if diff:
                    for mins in range(0, diff+1):
                        if momentum_count >= ppm:
                            momentum_count -= ppm
                        elif momentum_count <= -ppm:
                            momentum_count += ppm
                        elif (momentum_count > -ppm and momentum_count < 0) or (momentum_count < ppm and momentum_count > 0):
                            momentum_count = 0
                        else:
                            momentum_count = 0

                        if momentum_count < 0:
                            momentum.append([count, 0, None, None, momentum_count, None, None])

                        elif momentum_count > 0:
                            momentum.append([count, momentum_count, None, None, 0, None, None])
                        else:
                            momentum.append([count, 0,  None, None, 0, None, None])


                        # if team1_streak > 0:
                        #     if momentum_count >= ppm:
                        #         momentum_count -= ppm
                        #     else:
                        #         momentum_count = 0
                        #     momentum.append([count, momentum_count, None, None, 0, None, None])
                        # elif team2_streak > 0:
                        #     if momentum_count <= -ppm:
                        #         momentum_count += ppm
                        #     else:
                        #         momentum_count = 0
                        #     momentum.append([count, 0, None, None, momentum_count, None, None])
                        # else:
                        #     momentum.append([count, 0, 0, None, None, momentum_count, None, None])

                        count += 1

            if g.team == self.team_1:
                team_1_score += 1
                team1_streak += 1
                if momentum_count < 0:  #
                    if team2_streak > 1:
                        momentum_count = round(float(momentum_count) / float(3))    # cut m in half
                    else:
                        momentum_count = 0

                else:
                    momentum_count += ppg
                team2_streak = 0

            else:
                team_2_score += 1
                team2_streak += 1
                if momentum_count > 0:
                    if team1_streak > 1:
                        momentum_count = round(float(momentum_count)/float(3))
                    else:
                        momentum_count = 0

                else:
                    momentum_count -= ppg
                team1_streak = 0


            if momentum_count > 0:
                # momentum.append([count+1, momentum_count, 0])
                # count += 1
                if g.team == self.team_1:
                    momentum.append([count, momentum_count, 'G', "@ %s (%s-%s)" % (duration, team_1_score, team_2_score) , 0, None,None])
                else:
                    momentum.append([count, momentum_count, None, None, 0, 'G', "@ %s (%s-%s)" % (duration, team_1_score, team_2_score)])

            elif momentum_count == 0:
                # momentum.append([count+1, 0, 0])
                # count += 1
                if g.team == self.team_1:
                    momentum.append([count, 0, 'G', "@ %s (%s-%s)" % (duration, team_1_score, team_2_score), 0, None, None])
                else:
                    momentum.append([count, 0, None, None, 0, 'G', "@ %s (%s-%s)" % (duration, team_1_score, team_2_score)])

            else:
                # momentum.append([count+1, 0, momentum_count])
                # count += 1
                if g.team == self.team_1:
                    momentum.append([count, 0, 'G', "@ %s (%s-%s)" % (duration, team_1_score, team_2_score), momentum_count, None, None])
                else:
                    momentum.append([count, 0, None, None, momentum_count, 'G', "@ %s (%s-%s)" % (duration, team_1_score, team_2_score)])

            last_goal_date = g.created
            count += 1

        return json.dumps(momentum)

    @property
    def red_score(self):
        return self.goal_set.filter(team=self.team_1).aggregate(score=Sum('value'))['score'] or self.team_1_score or 0

    @property
    def black_score(self):
        return self.goal_set.filter(team=self.team_2).aggregate(score=Sum('value'))['score'] or self.team_2_score or 0

    _odds = ""
    @property
    def odds(self):
        from .utils import get_odds
        if not self._odds:
            self._odds = get_odds(self)
        return self._odds


class Goal(TimeStampedModel):
    match = models.ForeignKey(Match)
    value = models.IntegerField(_("Value"), default=1, help_text='corrections will be stored as -1')
    raspberry_pi = models.BooleanField(default=False)
    team = models.ForeignKey(Team, )

    class Meta:
        verbose_name = _("Goal")
        verbose_name_plural = _("Goals")
        ordering = ("created",)

    def __unicode(self):
        return '%s (%s)' % (self.match, self.value)
