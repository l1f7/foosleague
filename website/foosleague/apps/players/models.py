from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.db.models import Sum


class Player(TimeStampedModel):
    user = models.ForeignKey(User)
    nickname = models.CharField(_("Nickname"), max_length=200, blank=True, default="")

    ts_mu = models.FloatField(_("TrueSkill"), default=25, help_text = 'higher the better')
    ts_sigma = models.FloatField(_("TrueSkill Sigma"), default=8.333, help_text='basically an indicator of accuracy')
    ts_expose = models.FloatField(_("TrueSkill Expose"), default=0, help_text="Gets regenerated after ever match")
    photo = models.ImageField(_("Photo"), upload_to='players', blank=True, max_length=400, default="")
    slack_username = models.CharField(
        _("Slack Username"), blank=True, max_length=100, help_text="This will be used for any slack integrations", default="")

    #todo: move this to LeagueMember
    fooscoin = models.FloatField(_("FoosCoin"), default=500.00)

    class Meta:
        verbose_name = 'Player'
        verbose_name_plural = 'Players'
        ordering = ('-ts_expose',)

    def __unicode__(self):
        return '%s' % (self.nickname or self.user)

    def get_absolute_url(self):
        return reverse_lazy('player-detail', kwargs={'pk': self.id})

    def get_season_points(self, season=None):
        matches = StatHistory.objects.filter(player=self, season=season)
        points = matches.aggregate(points=Sum('season_points'))
        return points['points']


class StatHistory(TimeStampedModel):
    player = models.ForeignKey(Player)
    match = models.ForeignKey('matches.Match', blank=True, null=True)
    ts_mu = models.FloatField(_("TrueSkill"), default=25, help_text = 'higher the better')
    ts_sigma= models.FloatField(_("TrueSKill"), default=8.3333, help_text="Basically an indicator of accuracy")
    season = models.ForeignKey('seasons.Season', blank=True, null=True)
    season_points = models.IntegerField(_("Season Points"), blank=True, null=True)
    notes = models.TextField(_("Notes"), default="")

    class Meta:
        verbose_name = "Stat History"
        verbose_name_plural = "Stat Histories"
        ordering = ('-created',)

    def __unicode__(self):
        return '%s' % (self.created)
