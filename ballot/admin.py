from django.contrib import admin

##----------------------------------------------------------------------------##

from .models import (Party, UnitLevel, GovernmentalUnit, PrecinctArea,
					Election, Precinct, District, Office, Race,
					Candidate, Proposal)

admin.site.register(Party)
admin.site.register(UnitLevel)
admin.site.register(GovernmentalUnit)
admin.site.register(PrecinctArea)

admin.site.register(Election)
admin.site.register(Precinct) 
admin.site.register(District) 
admin.site.register(Office)
admin.site.register(Race)
admin.site.register(Candidate) 
admin.site.register(Proposal)