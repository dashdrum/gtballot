from django.conf.urls import patterns, url

from .views import PrecinctListView

urlpatterns = patterns('',

    url(r'^prec_list/', PrecinctListView.as_view(),name='prec_list'),
)
