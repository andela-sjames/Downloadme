# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


class Download(models.Model):
    """ Download class defined."""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = model.DateTimeField(auto_now=True)
    file_name = models.CharField(max_length=50)
    person = models.ForeignKeyField(User, on_delete=models.CASCADE, related_name='userdownload')
