# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import status
from rest_framework.response import response
from rest_framework.generics import ListCreateAPIView

from django.contrib.auth.models import User
from api.models import Download

from api.serializers import DownloadSerializer, UserSerializer

class UserListCreateView(ListCreateAPIView):
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DownloadListCreateView(ListCreateAPIView):
    model = Download
    queryset = Download.objects.all()
    serializer_class = DownloadSerializer
