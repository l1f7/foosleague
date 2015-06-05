from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel
from django.core.urlresolvers import reverse_lazy

from teams.models import Team
from seasons.models import Season
from leagues.models import League
# from players.models import Player
from .utils import update_trueskill


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

    def complete(self):
        if self.winner == self.team_1:
            self.team_2.streak = 0
            self.team_2.save()
            self.team_1.streak += 1
            self.team_1.save()
        else:
            self.team_1.streak = 0
            self.team_1.save()
            self.team_2.streak += 1
            self.team_2.save()

        update_trueskill(self)
