import json
from django.core import serializers
from datetime import datetime, timedelta

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.db.models import Sum, Q
from django.db.models.loading import get_model

from .utils import calc_wins, calc_loses, calc_goal_differential, calc_color_preference, calc_stats


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
    rfid_code = models.CharField(_("RFID Code"), blank=True, default="", help_text="RFID Card number", max_length=20)
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
        from seasons.models import Season
        today = datetime.today
        season = Season.objects.filter(start__lte=today, end__gte=today)
        try:
            return self.stathistory_set.filter(season=season).exclude(ts_mu=0)[0].ts_mu
        except:
            return 25

    @property
    def current_sigma(self):
        from seasons.models import Season
        today = datetime.today
        season = Season.objects.filter(start__lte=today, end__gte=today)
        try:
            return self.stathistory_set.filter(season=season).exclude(ts_sigma=0)[0].ts_sigma
        except:
            return 8.3333333333

    @property
    def current_expose(self):
        from seasons.models import Season
        today = datetime.today
        season = Season.objects.filter(start__lte=today, end__gte=today)
        try:
            return self.exposehistory_set.filter(season=season)[0].ts_expose
        except:
            return 0

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
        from seasons.models import Season

        today = datetime.today

        season = Season.objects.filter(start__lte=today, end__gte=today)

        obj = self.exposehistory_set.filter(season=season).filter(created__gte=datetime.today()-timedelta(days=30)).order_by('created').values_list('ts_expose', flat=True)
        leader = ExposeHistory.objects.filter(season=season).filter(created__gte=datetime.today()-timedelta(days=30), player=Player.objects.all()[0]).order_by('created').values_list('ts_expose', flat=True)

        r = []
        last = None
        for count, e in enumerate(obj):
            if e != last:
                r.append([count, e, leader[count]])
                last = e

        return r

    #todo: make this a template tag or something. has no bearing on current player
    @property
    def leader_expose(self):
        from seasons.models import Season
        today = datetime.today
        season = Season.objects.filter(start__lte=today, end__gte=today)

        obj = self.exposehistory_set.filter(created__gte=datetime.today()-timedelta(days=30), season=season).order_by('created').values_list('ts_expose', flat=True)
        leader = ExposeHistory.objects.filter(created__gte=datetime.today()-timedelta(days=30), season=season, player=Player.objects.all()[0]).order_by('created').values_list('ts_expose', flat=True)
        r = []
        last = None
        for count, e in enumerate(obj):
            if e != last:
                r.append([count, leader[count]])
                last = e

        return r

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
        from seasons.models import Season
        today = datetime.today
        season = Season.objects.filter(start__lte=today, end__gte=today)
        if not self._matches:
            self._matches = get_model('matches.Match').objects.filter(
                Q(team_1=self.teams) | Q(team_2=self.teams), season=season)

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
    def win_spanning_days(self):
        return self.streaks['win_spanning_days']

    @property
    def worst_losing_streak(self):
        return self.streaks['worst_losing_streak']

    @property
    def loss_spanning_days(self):
        return self.streaks['loss_spanning_days']

    @property
    def worst_losing_streak_date(self):
        return self.streaks['worst_losing_streak_date']

    @property
    def wins_7(self):
        return calc_wins(self, 7, season=True)

    @property
    def wins_30(self):
        return calc_wins(self, 30, season=True)

    @property
    def wins_season(self):
        return calc_wins(self, season=True)

    @property
    def loses_7(self):
        return calc_loses(self, 7, season=True)

    @property
    def loses_30(self):
        return calc_loses(self, 30, season=True)

    @property
    def loses_season(self):
        return calc_loses(self, season=True)

    @property
    def goals_for_7(self):
        return calc_goal_differential(self, 7, 'for', season=True)
    @property
    def goals_for_30(self):
        return calc_goal_differential(self, 30, 'for', season=True)
    @property
    def rgoals_for_season(self):
        return calc_goal_differential(self, direction='for', season=True)

    @property
    def goals_against_7(self):
        return calc_goal_differential(self, 7, 'against', season=True)
    @property
    def goals_against_30(self):
        return calc_goal_differential(self, 30, 'against', season=True)
    @property
    def goals_against_season(self):
        return calc_goal_differential(self, direction='against', season=True)

    _stats = ""
    @property
    def stats(self):
        if not self._stats:
            self._stats = calc_stats(self)

        return self._stats




class StatHistory(TimeStampedModel):
    player = models.ForeignKey(Player)
    match = models.ForeignKey('matches.Match', blank=True, null=True)

    ts_mu = models.FloatField(_("TrueSkill"), default=25, help_text='higher the better')
    ts_sigma = models.FloatField(
        _("TrueSkill Sigma"), default=8.3333, help_text="Basically an indicator of accuracy")

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


class ExposeHistory(TimeStampedModel):
    match = models.ForeignKey('matches.Match')
    ts_expose = models.FloatField(_("TrueSkill Expose"), default=0, help_text="leaderboard")
    player = models.ForeignKey('players.Player')

    season = models.ForeignKey('seasons.Season', blank=True, null=True, default=1)


    def __unicode__(self):
        return '%s' % (self.match)


