from django.conf.urls import url

from Bk.views import *

from . import views

app_name='Bk'
urlpatterns=[
    url(r'^$',index,name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$',detail,name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',views.archives,name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$',views.category,name='category'),
]

