import factory
#from datetime import date, time
from datetime import datetime, timedelta
try:
    from django.utils.timezone import now
except ImportError:
    from datetime.datetime import now

from ballot.models import (Party, UnitLevel, GovernmentalUnit, Municipality, 
                           Election, Precinct, Race, District, Proposal, 
                           Office, Candidate)

class PartyFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Party

    code = factory.Sequence(lambda n:  n, str)
    name = factory.Sequence(lambda n: 'Party' + n, str)

class UnitLevelFactory(factory.DjangoModelFactory):
    FACTORY_FOR = UnitLevel

    code = factory.Sequence(lambda n:  n, str)
    name = factory.Sequence(lambda n: 'UnitLevel' + n, str)

class GovernmentalUnitFactory(factory.DjangoModelFactory):
    FACTORY_FOR = GovernmentalUnit

    name = factory.Sequence(lambda n: 'GovernmentalUnit' + n, str)
    unit_level = factory.SubFactory(UnitLevelFactory)
    

class MunicipalityFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Municipality

    code = factory.Sequence(lambda n:  n, str)
    name = factory.Sequence(lambda n: 'Municipality' + n, str)
    

class ElectionFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Election

    name = factory.Sequence(lambda n: 'Election' + n, str)
    election_date = (now() + timedelta(days=100)).date()