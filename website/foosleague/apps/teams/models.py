from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel, ActivatorModel
# Create your models here.
from players.models import Player


class Team(TimeStampedModel):
    name = models.CharField(_("Name"), max_length=250, blank=True, default="")
    logo = models.ImageField(_("Logo"), upload_to='logos', max_length=500, blank=True, default="")

    player_1 = models.ForeignKey(Player, verbose_name=_("Player 1"), related_name='player_1')
    player_2 = models.ForeignKey(Player, verbose_name=_("Player 2"), related_name='player_2')

    class Meta:
        verbose_name = _('Team')
        verbose_name_plural = _('Teams')

    def __unicode__(self):
        if self.name != "":
            return '%s' % self.name
        return '%s & %s' % (self.player_1, self.player_2)
