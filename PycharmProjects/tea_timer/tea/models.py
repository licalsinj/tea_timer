# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class Tea(models.Model):
    user = models.ForeignKey(User, default=12)
    name = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    price = models.FloatField()
    rating = models.IntegerField()
    picture = models.FileField()
    origin = models.CharField(max_length=250)
    tasting_notes = models.CharField(max_length=1000)

    def get_absolute_url(self):
        return reverse('tea:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name + ' - ' + self.type


class WesternBrew(models.Model):
    tea = models.ForeignKey(Tea, on_delete=models.CASCADE)
    brew_name = models.CharField(max_length=100)
    water_qty = models.FloatField()
    temp_C = models.IntegerField()
    tea_qty = models.FloatField()
    min_brew_time = models.FloatField()
    max_brew_time = models.FloatField()

    def __str__(self):
        return self.tea.name + " " + self.brew_name + ' Western ' + str(self.pk)


class GongFuBrew(models.Model):
    tea = models.ForeignKey(Tea, on_delete=models.CASCADE)
    brew_name = models.CharField(max_length=100)
    gaiwan_size = models.FloatField()
    temp_C = models.IntegerField()
    tea_qty = models.FloatField()
    steep_num = models.IntegerField()
    steep_times_string = models.CharField(max_length=100)
    steep_times = ArrayField(models.IntegerField())

    def get_absolute_url(self):
        return reverse('tea:gfbrew-update', kwargs={'pk': self.pk})

    def __str__(self):
        return self.tea.name + " " + self.brew_name + " Gong Fu " + str(self.pk)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=254, blank=False)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
