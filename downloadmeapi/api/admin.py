# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.models import User

from .models import Download

# Register your models here.
admin.site.register(Download)
admin.site.register(User)



