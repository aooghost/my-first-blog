from django.conf.urls import url
from . import views

app_name ='music'

urlpatterns = [
    #/music
    url(r'^music$', views.index, name='index'),

    #/music/712/
    url(r'^music/(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

    #music/contact
    url(r'^contact/$', views.contact, name='contact'),

    url(r'^$', views.cover, name='cover'),
]
