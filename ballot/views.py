from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, FormView
from django.core.urlresolvers import reverse


from .models import Precinct, Candidate
from .forms import PrecinctSelectForm

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
		qs = qs.filter(race__office__district__precincts__id__in=precs.values_list('id'))
		qs = qs.filter(race__election__pk = election_id)
		qs = qs.order_by('race__office__district__name','race__office__name')
		
		return qs

class PrecinctSelectView(FormView):
	form_class = PrecinctSelectForm
	template_name = 'ballot/precinct_select.html'

	def form_valid(self,form):
		prec_id = form.cleaned_data.get('precinct').id
		return HttpResponseRedirect(reverse('prec_ballot', kwargs={'election_id': 1, 'prec_id': prec_id }))