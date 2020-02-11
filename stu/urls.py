#coding=utf-8

from django.conf.urls import url
import views

urlpatterns=[
    url(r'^$',views.IndexView.as_view()),
    url(r'^csrf/$',views.index2View)
]
