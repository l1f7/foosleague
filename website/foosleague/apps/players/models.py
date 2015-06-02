from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from teams.models import Team


class Player(TimeStampedModel):
    user = models.ForeignKey(User)
    nickname = models.CharField(_("Nickname"), max_length=200, blank=True, default="")

    trueskill = models.FloatField(_("TrueSkill"), default=20)
    photo = models.ImageField(_("Photo"), upload_to='players', blank=True, max_length=400, default="")
    slack_username = models.CharField(_("Slack  Username"), blank=True, max_length=100, help_text="This will be used for any slack integrations", default="")

    fooscoin = models.FloatField(_("FoosCoin"), default=500.00)

    class Meta:
        verbose_name = 'Player'
        verbose_name_plural = 'Players'

    def __unicode__(self):
        return '%s' % (self.nickname or self.user)

    def get_absolute_url(self):
        return reverse_lazy('player-detail', kwargs={'pk': self.id})
