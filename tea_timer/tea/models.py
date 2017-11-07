# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.


class Tea(models.Model):
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
    min_brew_time = models.TimeField()
    max_brew_time = models.TimeField()

    def __str__(self):
        return self.tea.name + " " + self.brew_name + ' Western ' + str(self.pk)


class GongFuBrew(models.Model):
    tea = models.ForeignKey(Tea, on_delete=models.CASCADE)
    brew_name = models.CharField(max_length=100)
    gaiwan_size = models.FloatField()
    temp_C = models.IntegerField()
    tea_qty = models.FloatField()
    steep_num = models.IntegerField()
    steep_times = models.CharField(max_length=1000)

    def get_absolute_url(self):
        return reverse('tea:gfbrew-update', kwargs={'pk': self.pk})

    def __str__(self):
        return self.tea.name + " " + self.brew_name + " Gong Fu " + str(self.pk)


