from django.conf.urls import patterns, url

from .views import PrecinctListView, PrecinctBallotView

urlpatterns = patterns('',

    url(r'^prec_list/', PrecinctListView.as_view(),name='prec_list'),
    url(r'^prec_ballot/(?P<election_id>\d+)/(?P<prec_id>\d+)/$', PrecinctBallotView.as_view(),name='prec_ballot'),
)
