import factory
#from datetime import date, time
from datetime import datetime, timedelta
try:
    from django.utils.timezone import now
except ImportError:
    from datetime.datetime import now

from ballot.models import (Party, UnitLevel, GovernmentalUnit, PrecinctArea, 
                           Election, Precinct, Race, District, Proposal, 
                           Office, Candidate)

class PartyFactory(factory.DjangoModelFactory):
    class Meta:
        model = Party

    code = factory.Sequence(lambda n:  n, str)
    name = factory.Sequence(lambda n: 'Party' + n, str)

class UnitLevelFactory(factory.DjangoModelFactory):
    class Meta:
        model = UnitLevel

    code = factory.Sequence(lambda n:  n, str)
    name = factory.Sequence(lambda n: 'UnitLevel' + n, str)

class GovernmentalUnitFactory(factory.DjangoModelFactory):
    class Meta:
        model = GovernmentalUnit

    name = factory.Sequence(lambda n: 'GovernmentalUnit' + n, str)
    unit_level = factory.SubFactory(UnitLevelFactory)
    

class PrecinctAreaFactory(factory.DjangoModelFactory):
    class Meta:
        model = PrecinctArea

    code = factory.Sequence(lambda n:  n, str)
    name = factory.Sequence(lambda n: 'PrecinctArea ' + n, str)
    

class ElectionFactory(factory.DjangoModelFactory):
    class Meta:
        model = Election

    name = factory.Sequence(lambda n: 'Election' + n, str)
    election_date = (now() + timedelta(days=100)).date()

class PrecinctFactory(factory.DjangoModelFactory):
    class Meta:
        model = Precinct

    prec_area = factory.SubFactory(PrecinctAreaFactory)
    prec_number = factory.Sequence(lambda n: n, str)
    polling_location = factory.Sequence(lambda n: "Location " + n, str)

class DistrictFactory(factory.DjangoModelFactory):
    class Meta:
        model = District

    name = factory.Sequence(lambda n: "District " + n, str)
    govt_unit = factory.SubFactory(GovernmentalUnitFactory)
    # precincts

class OfficeFactory(factory.DjangoModelFactory):
    class Meta:
        model = Office

    district = factory.SubFactory(DistrictFactory)
    name = factory.Sequence(lambda n: "Office " + n, str)

class RaceFactory(factory.DjangoModelFactory):
    class Meta:
        model = Race

    votes_allowed = factory.Sequence(lambda n: n, int)
    election = factory.SubFactory(ElectionFactory)
    office = factory.SubFactory(OfficeFactory)

class CandidateFactory(factory.DjangoModelFactory):
    class Meta:
        model = Candidate

    race = factory.SubFactory(RaceFactory)
    name = factory.Sequence(lambda n: "Candidate " + n, str)
    ticket_mate = None
    party = factory.SubFactory(PartyFactory)
    incumbent = False
    url = factory.Sequence(lambda n: 'http://example.com/' + n, str)

class ProposalFactory(factory.DjangoModelFactory):
    class Meta:
        model = Proposal

    district = factory.SubFactory(DistrictFactory)
    election = factory.SubFactory(ElectionFactory)
    title = factory.Sequence(lambda n: "Proposal " + n, str)
    text = factory.Sequence(lambda n: ("Lorem Ipsum " + n) * 100, str)

