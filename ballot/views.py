from django.shortcuts import render

from django.views.generic import ListView, DetailView

from .models import Precinct, Candidate

#------------------------------------------------------------------------------#

class PrecinctListView(ListView):

	model=Precinct

class PrecinctBallotView(ListView):

	model = Candidate
	template_name = 'ballot/precinct_ballot.html'

	def get_queryset(self):
		prec_id = self.kwargs.get('prec_id', None)
		election_id = self.kwargs.get('election_id', None)

		precs = Precinct.objects.filter(pk = prec_id)

		qs = Candidate.objects.all()
		qs = qs.filter(race__office__district__precints__id__in=precs.values_list('id'))
		qs = qs.filter(race__election__pk = election_id)
		qs = qs.order_by('race__office__district__name','race__office__name')
		
		return qs
