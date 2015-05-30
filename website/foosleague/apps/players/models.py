from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy

from teams.models import Team


class Player(TimeStampedModel):
    user = models.OneToOneField(User, blank=False)
    nickname = models.CharField(_("Nickname"), max_length=200, blank=True, default="")
    team = models.ForeignKey(Team)
    trueskill = models.FloatField(_("TrueSkill"), default=20)


    class Meta:
        verbose_name = 'Player'
        verbose_name_plural = 'Players'

    def __unicode__(self):
        return '%s' % (self.nickname or self.user)

    def get_absolute_url(self):
        return reverse_lazy('player-detail', kwargs={'pk': self.id})
