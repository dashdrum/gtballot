from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, FormView
from django.core.urlresolvers import reverse

from annoying.functions import get_object_or_None

from .models import Precinct, Candidate, Election
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

	def get_context_data(self, **kwargs):
		context = super(PrecinctBallotView,self).get_context_data(**kwargs)
		election = get_object_or_None(Election,pk=self.kwargs.get('election_id', None))
		precinct = get_object_or_None(Precinct,pk=self.kwargs.get('prec_id', None))
		context['election'] = election
		context['precinct'] = precinct
		return context

class PrecinctSelectView(FormView):
	form_class = PrecinctSelectForm
	template_name = 'ballot/precinct_select.html'

	def form_valid(self,form):
		prec_id = form.cleaned_data.get('precinct').id
		return HttpResponseRedirect(reverse('prec_ballot', kwargs={'election_id': 1, 'prec_id': prec_id }))