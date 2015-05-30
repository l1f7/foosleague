from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from players.models import Player
from matches.models import Match


class Bet(TimeStampedModel):
    amount = models.IntegerField(_("Amount"), default=0,)
    player = models.ForeignKey(Player)
    match = models.ForeignKey(Match)

    class Meta:
        verbose_name = _('Bet')
        verbose_name_plural = _('Bets')
        ordering = ('-created',)

    def __unicode__(self):
        return "%s (%s)" % (self.player, self.amount)

    def get_absolute_url(self):
        return reverse_lazy('bet-detail', kwargs={'pk': self.id})


class Transaction(TimeStampedModel):

    """
        Transaction, either a bet win, or a match win

    """
    amount = models.FloatField(_("Amount"), default=0.00)
    bet = models.ForeignKey(Bet, blank=True, null=True)
    match = models.ForeignKey(
        Match, blank=True, null=True, help_text='Match will be linked, if transaction amount came from a win')
    player = models.ForeignKey(Player)

    class Meta:
        verbose_name = _('Transaction')
        verbose_name_plural = _('Transactions')
        ordering = ('-created',)

    def __unicode__(self):
        return "%s (%s)" % (self.amount, self.player)
