from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel
from django.core.urlresolvers import reverse_lazy

from leagues.models import League

class Season(TimeStampedModel):

    """
        Seasons will encapsulate a series of matches.
        Leaderboards & fooscoin (?) will reset after "end" date.
        Trueskill will be retained
    """
    name = models.CharField(_("Name"), blank=False, default="", max_length=250, help_text='Season Name')
    start = models.DateField(_("Season Start"), blank=False)
    end = models.DateField(_("Season End"), blank=False)

    league = models.ForeignKey(League, default=1)

    class Meta:
        verbose_name = _("Season")
        verbose_name_plural = _("Seasons")

    def __unicode__(self):
        return '%s' % self.name

