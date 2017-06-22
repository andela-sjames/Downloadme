from django.conf.urls import url, include
from api import views

urlpatterns = [
    url(r'users/$', views.UserListCreateView.as_view(), name='api_users'),
    url(r'downloads/$', views.DownloadListCreateView.as_view(), name='api_downloads'),
]
