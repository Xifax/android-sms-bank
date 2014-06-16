# coding: utf-8
from django.db import models
from django.contrib.auth.models import User


class Device(models.Model):
    """Android device on the internal network"""
    ip = models.GenericIPAddressField(unique=True)
    online = models.NullBooleanField(default=False, blank=True)

    class Meta:
        verbose_name = u'устройство'
        verbose_name_plural = u'устройства'

    def __unicode__(self):
        return u'%s [%s]' % (self.ip, u'онлайн' if self.online else u'оффлайн')


class Profile(models.Model):
    """Lists devices associated with user"""
    user = models.ForeignKey(User, related_name='profile')
    devices = models.ManyToManyField(
        Device,
        related_name='profiles',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = u'профиль'
        verbose_name_plural = u'профили'

    def __unicode__(self):
        return u'%s' % self.user.username
        # return u'%s' % u', '.join([str(d) for d in self.devices])
