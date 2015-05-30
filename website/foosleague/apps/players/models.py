from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel
from django.contrib.auth.models import User


class Player(TimeStampedModel):
    user = models.OneToOneField(User, blank=False)
    nickname = models.CharField(_("Nickname"), max_length=200, blank=True, default="")

    class Meta:
        verbose_name = 'Player'
        verbose_name_plural = 'Players'

    def __unicode__(self):
        return '%s' % (self.nickname or self.user)
