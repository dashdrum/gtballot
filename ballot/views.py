from django.shortcuts import render

from django.views.generic import ListView

from .models import Precinct

#------------------------------------------------------------------------------#

class PrecinctListView(ListView):

	model=Precinct
