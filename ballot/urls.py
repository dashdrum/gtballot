from django.conf.urls import patterns, url
from django.views.generic import RedirectView

from .views import PrecinctListView, PrecinctBallotView, PrecinctSelectView, GetPrecinctOptionsView

urlpatterns = patterns('',

    url(r'^prec_list/', PrecinctListView.as_view(),name='prec_list'),
    url(r'^prec_select/', PrecinctSelectView.as_view(),name='prec_select'),
    url(r'^prec_ballot/(?P<election_id>\d+)/(?P<prec_id>\d+)/$', PrecinctBallotView.as_view(),name='prec_ballot'),
    url(r'^prec_options/(?P<prec_area>\d+)/$', GetPrecinctOptionsView.as_view(), name = 'prec_options'),

    (r'^$', RedirectView.as_view(url='prec_select')),
)
