from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel
from django_extensions.db.fields import AutoSlugField
from players.models import Player


class League(TimeStampedModel):
    name = models.CharField(_("Name"), max_length=250)
    photo = models.ImageField(_("Photo"), upload_to='leagues', max_length=250)
    subdomain = AutoSlugField(_('subdomain'), populate_from='name')

    slack_token = models.CharField(_("Slack Token"), max_length=100, default="", blank=True, help_text="Slack Bot Authentication Token")
    slack_channel = models.CharField(
        _("Slack Channel"), max_length=50, default="", blank=True, help_text='Slack channel you would like foosleague to broadcast to.')

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



# TODO:

# HouseRules
# Milestones
