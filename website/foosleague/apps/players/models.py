from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.db.models import Sum, Q
from django.db.models.loading import get_model


class Player(TimeStampedModel):
    user = models.ForeignKey(User)
    nickname = models.CharField(_("Nickname"), max_length=200, blank=True, default="")

    ts_mu = models.FloatField(_("TrueSkill"), default=25, help_text='higher the better')
    ts_sigma = models.FloatField(
        _("TrueSkill Sigma"), default=8.333, help_text='basically an indicator of accuracy')
    ts_expose = models.FloatField(
        _("TrueSkill Expose"), default=0, help_text="Gets regenerated after ever match")
    photo = models.ImageField(_("Photo"), upload_to='players', blank=True, max_length=400, default="")
    slack_username = models.CharField(
        _("Slack Username"), blank=True, max_length=100, help_text="This will be used for any slack integrations", default="")

    # todo: move this to LeagueMember
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

    @property
    def current_mu(self):
        try:
            return self.stathistory_set.all().order_by('created')[0].ts_mu
        except:
            return 25

    @property
    def current_sigma(self):
        try:
            return self.stathistory_set.all().order_by('created')[0].ts_sigma
        except:
            return 8.3333333333

    @property
    def current_expose(self):
        return self.stathistory_set.all()[0].ts_expose

    @property
    def current_fooscoin(self):
        return self.stathistory_set.all().aggregate(fooscoin=Sum('fooscoin'))['fooscoin']

    @property
    def full_mu(self):
        return self.stathistory_set.all().values_list('created', 'ts_mu')

    @property
    def full_sigma(self):
        return self.stathistory_set.all().values_list('created', 'ts_sigma')

    @property
    def full_expose(self):
        return self.stathistory_set.all().values_list('created', 'ts_expose')

    @property
    def full_fooscoin(self):
        return self.stathistory_set.all().values_list('created', 'fooscoin')

    _teams = ""

    @property
    def teams(self):
        if not self._teams:
            self._teams = get_model('teams.Team').objects.filter(players=self)

        return self._teams

    _matches = ""

    @property
    def matches(self):
        if not self._matches:
            self._matches = get_model('matches.Match').objects.filter(
                Q(team_1=self.teams) | Q(team_2=self.teams))

        return self._matches

    _streaks = ""

    @property
    def streaks(self):
        if not self._streaks:
            from .utils import get_streaks
            self._streaks = get_streaks(self)
        return self._streaks

    @property
    def best_win_streak(self):
        return self.streaks['best_win_streak']

    @property
    def best_win_streak_date(self):
        return self.streaks['best_win_streak_date']

    @property
    def losing_streak(self):
        return self.streaks['losing_streak']

    @property
    def not_lost_since(self):
        return self.streaks['not_lost_since']

    @property
    def not_won_since(self):
        return self.streaks['not_won_since']

    @property
    def win_streak(self):
        return self.streaks['win_streak']

    @property
    def worst_losing_streak(self):
        return self.streaks['worst_losing_streak']

    @property
    def worst_losing_streak_date(self):
        return self.streaks['worst_losing_streak_date']


class StatHistory(TimeStampedModel):
    player = models.ForeignKey(Player)
    match = models.ForeignKey('matches.Match', blank=True, null=True)

    ts_mu = models.FloatField(_("TrueSkill"), default=25, help_text='higher the better')
    ts_sigma = models.FloatField(
        _("TrueSkill Sigma"), default=8.3333, help_text="Basically an indicator of accuracy")
    ts_expose = models.FloatField(_("TrueSkill Expose"), default=0, help_text="Leaderboard")

    season = models.ForeignKey('seasons.Season', blank=True, null=True)
    season_points = models.IntegerField(_("Season Points"), blank=True, null=True)

    fooscoin = models.FloatField(_("Fooscoin"), blank=True, null=True)

    notes = models.TextField(_("Notes"), default="")

    class Meta:
        verbose_name = "Stat History"
        verbose_name_plural = "Stat Histories"
        ordering = ('-created',)

    def __unicode__(self):
        return '%s' % (self.created)
