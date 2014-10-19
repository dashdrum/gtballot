
from django.test import TestCase    
from django.db import IntegrityError
from django.core.exceptions import ValidationError
#from datetime import date, time
from datetime import datetime, timedelta

    
from .factories import (PartyFactory, UnitLevelFactory, GovernmentalUnitFactory, 
	                    MunicipalityFactory, ElectionFactory, PrecinctFactory, 
	                    DistrictFactory, OfficeFactory, RaceFactory, 
	                    CandidateFactory, ProposalFactory)

#### Testing the Models


class BallotTestCase(TestCase):
    pass

class TestPartyModel(BallotTestCase):

    def test_unicode_value(self):
        p = PartyFactory.create()
        self.assertEqual(p.__unicode__(), p.name)
        
    def test_allow_delete(self):
        p = PartyFactory.create()
        self.assertTrue(p.allow_delete)

class TestUnitLevelModel(BallotTestCase):

    def test_unicode_value(self):
        p = UnitLevelFactory.create()
        self.assertEqual(p.__unicode__(), p.name)
        
    def test_allow_delete(self):
        p = UnitLevelFactory.create()
        self.assertTrue(p.allow_delete)

class TestGovernmentalUnitModel(BallotTestCase):

    def test_unicode_value(self):
        p = GovernmentalUnitFactory.create()
        self.assertEqual(p.__unicode__(), p.name)
        
    def test_allow_delete(self):
        p = GovernmentalUnitFactory.create()
        self.assertTrue(p.allow_delete)

class TestMunicipalityModel(BallotTestCase):

    def test_unicode_value(self):
        p = MunicipalityFactory.create()
        self.assertEqual(p.__unicode__(), p.name)
        
    def test_allow_delete(self):
        p = MunicipalityFactory.create()
        self.assertTrue(p.allow_delete)

class TestElectionModel(BallotTestCase):

    def test_unicode_value(self):
        p = ElectionFactory.create()
        self.assertEqual(p.__unicode__(), p.name)
        
    def test_allow_delete(self):
        p = ElectionFactory.create()
        self.assertTrue(p.allow_delete)

class TestPrecinctModel(BallotTestCase):

    def test_unicode_value(self):
        p = PrecinctFactory.create()
        self.assertEqual(p.__unicode__(), p.municipality.code + ' ' + p.prec_number)
        
    def test_allow_delete(self):
        p = PrecinctFactory.create()
        self.assertTrue(p.allow_delete)

class TestDistrictModel(BallotTestCase):

    def test_unicode_value(self):
        p = DistrictFactory.create()
        self.assertEqual(p.__unicode__(), p.name)
        
    def test_allow_delete(self):
        p = DistrictFactory.create()
        self.assertTrue(p.allow_delete)

class TestOfficeModel(BallotTestCase):

    def test_unicode_value(self):
        p = OfficeFactory.create()
        self.assertEqual(p.__unicode__(), p.district.__unicode__() + ' ' + p.name)
        
    def test_allow_delete(self):
        p = OfficeFactory.create()
        self.assertTrue(p.allow_delete)

class TestRaceModel(BallotTestCase):

    def test_unicode_value(self):
        p = RaceFactory.create()
        self.assertEqual(p.__unicode__(), p.election.__unicode__() + ' ' + p.office.__unicode__())
        
    def test_allow_delete(self):
        p = RaceFactory.create()
        self.assertTrue(p.allow_delete)

class TestCandidateModel(BallotTestCase):

    def test_unicode_value(self):
        p = CandidateFactory.create()
        self.assertEqual(p.__unicode__(), p.name)
        
    def test_allow_delete(self):
        p = CandidateFactory.create()
        self.assertTrue(p.allow_delete)

class TestProposalModel(BallotTestCase):

    def test_unicode_value(self):
        p = ProposalFactory.create()
        self.assertEqual(p.__unicode__(), p.title)
        
    def test_allow_delete(self):
        p = ProposalFactory.create()
        self.assertTrue(p.allow_delete)

