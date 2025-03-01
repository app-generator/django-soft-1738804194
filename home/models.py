# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    two_factor_enabled = models.TextField(max_length=255, null=True, blank=True)
    otp_secret = models.TextField(max_length=255, null=True, blank=True)
    phone_number = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Gift_List(models.Model):

    #__Gift_List_FIELDS__
    recipitent = models.CharField(max_length=255, null=True, blank=True)
    creator = models.CharField(max_length=255, null=True, blank=True)
    view_status = models.ForeignKey(Autofill, on_delete=models.CASCADE)
    description = models.TextField(max_length=255, null=True, blank=True)
    ranking = models.ForeignKey(Autofill, on_delete=models.CASCADE)

    #__Gift_List_FIELDS__END

    class Meta:
        verbose_name        = _("Gift_List")
        verbose_name_plural = _("Gift_List")


class Autofill(models.Model):

    #__Autofill_FIELDS__
    view_status = models.CharField(max_length=255, null=True, blank=True)
    ranking = models.CharField(max_length=255, null=True, blank=True)

    #__Autofill_FIELDS__END

    class Meta:
        verbose_name        = _("Autofill")
        verbose_name_plural = _("Autofill")


class Group(models.Model):

    #__Group_FIELDS__
    group_name = models.CharField(max_length=255, null=True, blank=True)
    group_active = models.BooleanField()
    group_admin = models.CharField(max_length=255, null=True, blank=True)
    group_description = models.TextField(max_length=255, null=True, blank=True)

    #__Group_FIELDS__END

    class Meta:
        verbose_name        = _("Group")
        verbose_name_plural = _("Group")



#__MODELS__END
