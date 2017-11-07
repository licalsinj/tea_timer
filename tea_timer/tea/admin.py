# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Tea, WesternBrew, GongFuBrew
from django.contrib import admin

# Register your models here.
admin.site.register(Tea)
admin.site.register(WesternBrew)
admin.site.register(GongFuBrew)
