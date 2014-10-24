from __future__ import unicode_literals

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

    def test_str_value(self):
        p = PartyFactory.create()
        self.assertEqual(p.__str__(), p.name)
        
    def test_allow_delete(self):
        p = PartyFactory.create()
        self.assertTrue(p.allow_delete)

        c = CandidateFactory.create(party=p)
        self.assertFalse(p.allow_delete)

class TestUnitLevelModel(BallotTestCase):

    def test_str_value(self):
        u = UnitLevelFactory.create()
        self.assertEqual(u.__str__(), u.name)
        
    def test_allow_delete(self):
        u = UnitLevelFactory.create()
        self.assertTrue(u.allow_delete)

        g = GovernmentalUnitFactory.create(unit_level=u)
        self.assertFalse(u.allow_delete)

class TestGovernmentalUnitModel(BallotTestCase):

    def test_str_value(self):
        g = GovernmentalUnitFactory.create()
        self.assertEqual(g.__str__(), g.name)
        
    def test_allow_delete(self):
        g = GovernmentalUnitFactory.create()
        self.assertTrue(g.allow_delete)

        d = DistrictFactory.create(govt_unit=g)
        self.assertFalse(g.allow_delete)

class TestMunicipalityModel(BallotTestCase):

    def test_str_value(self):
        m = MunicipalityFactory.create()
        self.assertEqual(m.__str__(), m.name)
        
    def test_allow_delete(self):
        m = MunicipalityFactory.create()
        self.assertTrue(m.allow_delete)

        pr = PrecinctFactory.create(municipality=m)
        self.assertFalse(m.allow_delete)

class TestElectionModel(BallotTestCase):

    def test_str_value(self):
        e = ElectionFactory.create()
        self.assertEqual(e.__str__(), e.name)
        
    def test_allow_delete(self):
        e = ElectionFactory.create()
        self.assertTrue(e.allow_delete)

        r = RaceFactory.create(election=e)
        self.assertFalse(e.allow_delete)

        e2 = ElectionFactory.create()
        pp = ProposalFactory.create(election=e2)
        self.assertFalse(e2.allow_delete)

class TestPrecinctModel(BallotTestCase):

    def test_str_value(self):
        pr = PrecinctFactory.create()
        self.assertEqual(pr.__str__(), pr.municipality.code + ' ' + pr.prec_number)
        
    def test_allow_delete(self):
        pr = PrecinctFactory.create()
        self.assertTrue(pr.allow_delete)

        d = DistrictFactory.create()
        d.precints.add(pr)
        d.save()
        self.assertFalse(pr.allow_delete)


class TestDistrictModel(BallotTestCase):

    def test_str_value(self):
        d = DistrictFactory.create()
        self.assertEqual(d.__str__(), d.name)
        
    def test_allow_delete(self):
        d = DistrictFactory.create()
        self.assertTrue(d.allow_delete)

        o = OfficeFactory.create(district=d)
        self.assertFalse(d.allow_delete)

        d2 = DistrictFactory.create()
        pp = ProposalFactory.create(district=d2)
        self.assertFalse(d.allow_delete)

class TestOfficeModel(BallotTestCase):

    def test_str_value(self):
        o = OfficeFactory.create()
        self.assertEqual(o.__str__(), o.district.__str__() + ' ' + o.name)
        
    def test_allow_delete(self):
        o = OfficeFactory.create()
        self.assertTrue(o.allow_delete)

        r = RaceFactory.create(office=o)
        self.assertFalse(o.allow_delete)

class TestRaceModel(BallotTestCase):

    def test_str_value(self):
        r = RaceFactory.create()
        self.assertEqual(r.__str__(), r.election.__str__() + ' ' + r.office.__str__())
        
    def test_allow_delete(self):
        r = RaceFactory.create()
        self.assertTrue(r.allow_delete)

        c = CandidateFactory.create(race=r)
        self.assertFalse(r.allow_delete)

class TestCandidateModel(BallotTestCase):

    def test_str_value(self):
        p = CandidateFactory.create()
        self.assertEqual(p.__str__(), p.name)
        
    def test_allow_delete(self):
        p = CandidateFactory.create()
        self.assertTrue(p.allow_delete)

class TestProposalModel(BallotTestCase):

    def test_str_value(self):
        p = ProposalFactory.create()
        self.assertEqual(p.__str__(), p.title)
        
    def test_allow_delete(self):
        p = ProposalFactory.create()
        self.assertTrue(p.allow_delete)

