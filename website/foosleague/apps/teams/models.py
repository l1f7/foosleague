from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel
from django.core.urlresolvers import reverse_lazy

from leagues.models import League

class Team(TimeStampedModel):
    name = models.CharField(_("Name"), max_length=250, blank=True, default="")
    logo = models.ImageField(_("Logo"), upload_to='logos', max_length=500, blank=True, default="")

    # player_1 = models.ForeignKey(Player, verbose_name=_("Player 1"), related_name='player_1')
    # player_2 = models.ForeignKey(Player, verbose_name=_("Player 2"), related_name='player_2')

    players = models.ManyToManyField("players.Player")
    trueskill_mu = models.FloatField(_("TrueSkill"), default=20)
    trueskill_sigma = models.FloatField(_("TrueSkill Sigma"), default=8.33)
    streak = models.IntegerField(
        _("Current Streak"), default=0, help_text='De-normalized field to help with slack integration')
    best_streak = models.IntegerField(_("Best Streak"), default=0, help_text="The best streak every acheived by this team")
    best_streak_date = models.DateTimeField(_("Best Streak Date"), blank=True, null=True, help_text="The date of the last win")

    league = models.ForeignKey(League, verbose_name=_("League"), default=1)


    class Meta:
        verbose_name = _('Team')
        verbose_name_plural = _('Teams')
        ordering = ('-streak',)

    def __unicode__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse_lazy('team-detail', kwargs={'pk': self.id})
