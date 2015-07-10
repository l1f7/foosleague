from django.db import models

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy
from django_extensions.db.models import TimeStampedModel
from django_extensions.db.fields import AutoSlugField

from players.models import Player
from matches.models import Match


class FanHistory(TimeStampedModel):

    player = models.ForeignKey(Player,)
    match = models.ForeignKey(Match, blank=True, null=True)
    fans = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Fan History"
        verbose_name_plural = "Fan History"

    def __unicode__(self):
        return '%s' % (self.player,)


class FantasySetting(TimeStampedModel):
    player = models.ForeignKey(Player,)
    ticket_price = models.PositiveIntegerField(default=50)

    class Meta:
        verbose_name = "Fantasy Setting"
        verbose_name_plural = "Fantasy Settings"

    def __unicode__(self):
        return '%s' % (self.player,)

