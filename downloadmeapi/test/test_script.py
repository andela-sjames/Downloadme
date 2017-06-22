import time

from rest_framework.test import APITestCase
from rest_framework import status

from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from api.models import Download


class SetupModelInstanceTestCase(APITestCase):

    def setUp(self):
        self.user = User(first_name='usera', last_name='cool', username='my_user',
                        password='123456', is_staff=True)

        self.download = Download(person=self.user, file_name='the.pdf')


class UserDownloadTestCase(SetupModelInstanceTestCase):
     
     def test_download_can_retrieved(self):
         
         url = reverse('api_downloads')
         response = self.client.get(url)

         self.assertTrue(status.is_success(response.status_code))
         self.assertEqual(response.status_code, status.HTTP_200_OK)
         
     def test_user_can_be_retrieved(self):

        url = reverse('api_downloads')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
