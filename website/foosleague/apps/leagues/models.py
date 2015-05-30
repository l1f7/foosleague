from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel
from django.core.urlresolvers import reverse_lazy

from players.models import Player


class League(TimeStampedModel):
    name = models.CharField(_("Name"), max_length=250)
    photo = models.ImageField(_("Photo"), upload_to='leagues', max_length=250)

    class Meta:
        verbose_name = 'League'
        verbose_name_plural = 'Leagues'

    def __unicode__(self):
        return self.name


class LeagueMember(TimeStampedModel):
    league = models.ForeignKey(League, verbose_name=_("League"),)
    player = models.ForeignKey(Player, verbose_name=_("Player"))

    class Meta:
        verbose_name = 'League Member'
        verbose_name_plural = 'League Members'

    def __unicode__(self):
        return '%s (%s)' % (self.player, self.league,)