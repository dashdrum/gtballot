from __future__ import unicode_literals

from django.test import TestCase    
from django.db import IntegrityError
from django.core.exceptions import ValidationError
#from datetime import date, time
from datetime import datetime, timedelta

    
from .factories import (PartyFactory, UnitLevelFactory, GovernmentalUnitFactory, 
	                    PrecinctAreaFactory, ElectionFactory, PrecinctFactory, 
	                    DistrictFactory, OfficeFactory, RaceFactory, 
	                    CandidateFactory, ProposalFactory)

from ballot.models import (Party, UnitLevel, GovernmentalUnit, PrecinctArea,
                           Election, Precinct, District, Office, Race,
                           Candidate, Proposal)

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

    def test_sort_order(self):
        p1 = PartyFactory.create(code='A',name='Alpha',sort_order=2)
        p2 = PartyFactory.create(code='Z',name='Omega',sort_order=1)
        self.assertEqual(Party.objects.all()[0],p2)

    def test_sort_order_2(self):
        p3 = PartyFactory.create(code='A',name='Alpha')
        p4 = PartyFactory.create(code='Z',name='Omega')
        self.assertEqual(Party.objects.all()[0],p3)

    def test_sort_order_3(self):
        ## NULL sorts before a sort_order value 
        p5 = PartyFactory.create(code='A',name='Alpha')
        p6 = PartyFactory.create(code='Z',name='Omega',sort_order=1)
        self.assertEqual(Party.objects.all()[0],p5)

class TestUnitLevelModel(BallotTestCase):

    def test_str_value(self):
        u = UnitLevelFactory.create()
        self.assertEqual(u.__str__(), u.name)
        
    def test_allow_delete(self):
        u = UnitLevelFactory.create()
        self.assertTrue(u.allow_delete)

        g = GovernmentalUnitFactory.create(unit_level=u)
        self.assertFalse(u.allow_delete)

    def test_sort_order(self):
        u1 = UnitLevelFactory.create(code='A',name='Alpha',sort_order=2)
        u2 = UnitLevelFactory.create(code='Z',name='Omega',sort_order=1)
        self.assertEqual(UnitLevel.objects.all()[0],u2)

    def test_sort_order_2(self):
        u3 = UnitLevelFactory.create(code='A',name='Alpha')
        u4 = UnitLevelFactory.create(code='Z',name='Omega')
        self.assertEqual(UnitLevel.objects.all()[0],u3)

    def test_sort_order_3(self):
        ## NULL sorts before a sort_order value 
        u5 = UnitLevelFactory.create(code='A',name='Alpha')
        u6 = UnitLevelFactory.create(code='Z',name='Omega',sort_order=1)
        self.assertEqual(UnitLevel.objects.all()[0],u5)

class TestGovernmentalUnitModel(BallotTestCase):

    def test_str_value(self):
        g = GovernmentalUnitFactory.create()
        self.assertEqual(g.__str__(), g.name)
        
    def test_allow_delete(self):
        g = GovernmentalUnitFactory.create()
        self.assertTrue(g.allow_delete)

        d = DistrictFactory.create(govt_unit=g)
        self.assertFalse(g.allow_delete)

    def test_sort_order(self):
        g1 = GovernmentalUnitFactory.create(name='Alpha',sort_order=2)
        g2 = GovernmentalUnitFactory.create(name='Omega',sort_order=1)
        self.assertEqual(GovernmentalUnit.objects.all()[0],g2)

    def test_sort_order_2(self):
        g3 = GovernmentalUnitFactory.create(name='Alpha')
        g4 = GovernmentalUnitFactory.create(name='Omega')
        self.assertEqual(GovernmentalUnit.objects.all()[0],g3)

    def test_sort_order_3(self):
        ## NULL sorts before a sort_order value 
        g5 = GovernmentalUnitFactory.create(name='Alpha')
        g6 = GovernmentalUnitFactory.create(name='Omega',sort_order=1)
        self.assertEqual(GovernmentalUnit.objects.all()[0],g5)

class TestPrecinctAreaModel(BallotTestCase):

    def test_str_value(self):
        pa = PrecinctAreaFactory.create()
        self.assertEqual(pa.__str__(), pa.name)
        
    def test_allow_delete(self):
        pa = PrecinctAreaFactory.create()
        self.assertTrue(pa.allow_delete)

        pr = PrecinctFactory.create(prec_area=pa)
        self.assertFalse(pa.allow_delete)

    def test_sort_order(self):
        pa1 = PrecinctAreaFactory.create(code='A',name='Alpha',sort_order=2)
        pa2 = PrecinctAreaFactory.create(code='Z',name='Omega',sort_order=1)
        self.assertEqual(PrecinctArea.objects.all()[0],pa2)

    def test_sort_order_2(self):
        pa3 = PrecinctAreaFactory.create(code='A',name='Alpha')
        pa4 = PrecinctAreaFactory.create(code='Z',name='Omega')
        self.assertEqual(PrecinctArea.objects.all()[0],pa3)

    def test_sort_order_3(self):
        ## NULL sorts before a sort_order value 
        pa5 = PrecinctAreaFactory.create(code='A',name='Alpha')
        pa6 = PrecinctAreaFactory.create(code='Z',name='Omega',sort_order=1)
        self.assertEqual(PrecinctArea.objects.all()[0],pa5)

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

    def test_sort_order(self):
        e1 = ElectionFactory.create(election_date=datetime.now(),sort_order=2)
        e2 = ElectionFactory.create(election_date=datetime.now()+timedelta(days=1),sort_order=1)
        self.assertEqual(Election.objects.all()[0],e2)

    def test_sort_order_2(self):
        e3 = ElectionFactory.create(election_date=datetime.now())
        e4 = ElectionFactory.create(election_date=datetime.now()+timedelta(days=1))
        self.assertEqual(Election.objects.all()[0],e3)

    def test_sort_order_3(self):
        ## NULL sorts before a sort_order value 
        e5 = ElectionFactory.create(election_date=datetime.now())
        e6 = ElectionFactory.create(election_date=datetime.now()+timedelta(days=1),sort_order=1)
        self.assertEqual(Election.objects.all()[0],e5)

class TestPrecinctModel(BallotTestCase):

    def test_str_value(self):
        pr = PrecinctFactory.create()
        self.assertEqual(pr.__str__(), pr.prec_area.code + pr.prec_number)
        
    def test_allow_delete(self):
        pr = PrecinctFactory.create()
        self.assertTrue(pr.allow_delete)

        d = DistrictFactory.create()
        d.precincts.add(pr)
        d.save()
        self.assertFalse(pr.allow_delete)

    def test_sort_order(self):
        pr1 = PrecinctFactory.create(prec_number='01',sort_order=2)
        pr2 = PrecinctFactory.create(prec_number='02',sort_order=1)
        self.assertEqual(Precinct.objects.all()[0],pr2)

    def test_sort_order_2(self):
        pr3 = PrecinctFactory.create(prec_number='01')
        pr4 = PrecinctFactory.create(prec_number='02')
        self.assertEqual(Precinct.objects.all()[0],pr3)

    def test_sort_order_3(self):
        ## NULL sorts before a sort_order value 
        pr5 = PrecinctFactory.create(prec_number='01')
        pr6 = PrecinctFactory.create(prec_number='02',sort_order=1)
        self.assertEqual(Precinct.objects.all()[0],pr5)


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

    def test_sort_order(self):
        d1 = DistrictFactory.create(name='Alpha',sort_order=2)
        d2 = DistrictFactory.create(name='Omega',sort_order=1)
        self.assertEqual(District.objects.all()[0],d2)

    def test_sort_order_2(self):
        d3 = DistrictFactory.create(name='Alpha')
        d4 = DistrictFactory.create(name='Omega')
        self.assertEqual(District.objects.all()[0],d3)

    def test_sort_order_3(self):
        ## NULL sorts before a sort_order value 
        d5 = DistrictFactory.create(name='Alpha')
        d6 = DistrictFactory.create(name='Omega',sort_order=1)
        self.assertEqual(District.objects.all()[0],d5)

class TestOfficeModel(BallotTestCase):

    def test_str_value(self):
        o = OfficeFactory.create()
        self.assertEqual(o.__str__(), o.district.__str__() + ' ' + o.name)
        
    def test_allow_delete(self):
        o = OfficeFactory.create()
        self.assertTrue(o.allow_delete)

        r = RaceFactory.create(office=o)
        self.assertFalse(o.allow_delete)

    def test_sort_order(self):
        o1 = OfficeFactory.create(name='Alpha',sort_order=2)
        o2 = OfficeFactory.create(name='Omega',sort_order=1)
        self.assertEqual(Office.objects.all()[0],o2)

    def test_sort_order_2(self):
        o3 = OfficeFactory.create(name='Alpha')
        o4 = OfficeFactory.create(name='Omega')
        self.assertEqual(Office.objects.all()[0],o3)

    def test_sort_order_3(self):
        ## NULL sorts before a sort_order value 
        o5 = OfficeFactory.create(name='Alpha')
        o6 = OfficeFactory.create(name='Omega',sort_order=1)
        self.assertEqual(Office.objects.all()[0],o5)

class TestRaceModel(BallotTestCase):

    def setUp(self):
        super(TestRaceModel,self).setUp()
        self.o1 = OfficeFactory.create(name='Alpha')
        self.o2 = OfficeFactory.create(name='Omega')

    def test_str_value(self):
        r = RaceFactory.create()
        self.assertEqual(r.__str__(), r.election.__str__() + ' ' + r.office.__str__())
        
    def test_allow_delete(self):
        r = RaceFactory.create()
        self.assertTrue(r.allow_delete)

        c = CandidateFactory.create(race=r)
        self.assertFalse(r.allow_delete)

    def test_sort_order(self):
        r1 = RaceFactory.create(office=self.o1,sort_order=2)
        r2 = RaceFactory.create(office=self.o2,sort_order=1)
        self.assertEqual(Race.objects.all()[0],r2)

    def test_sort_order_2(self):
        r3 = RaceFactory.create(office=self.o1)
        r4 = RaceFactory.create(office=self.o2)
        self.assertEqual(Race.objects.all()[0],r3)

    def test_sort_order_3(self):
        ## NULL sorts before a sort_order value 
        r5 = RaceFactory.create(office=self.o1)
        r6 = RaceFactory.create(office=self.o2,sort_order=1)
        self.assertEqual(Race.objects.all()[0],r5)

class TestCandidateModel(BallotTestCase):

    def test_str_value(self):
        p = CandidateFactory.create()
        self.assertEqual(p.__str__(), p.name)
        
    def test_allow_delete(self):
        p = CandidateFactory.create()
        self.assertTrue(p.allow_delete)

    def test_sort_order(self):
        c1 = CandidateFactory.create(name='Alpha',sort_order=2)
        c2 = CandidateFactory.create(name='Omega',sort_order=1)
        self.assertEqual(Candidate.objects.all()[0],c2)

    def test_sort_order_2(self):
        c3 = CandidateFactory.create(name='Alpha')
        c4 = CandidateFactory.create(name='Omega')
        self.assertEqual(Candidate.objects.all()[0],c3)

    def test_sort_order_3(self):
        ## NULL sorts before a sort_order value 
        c5 = CandidateFactory.create(name='Alpha')
        c6 = CandidateFactory.create(name='Omega',sort_order=1)
        self.assertEqual(Candidate.objects.all()[0],c5)

class TestProposalModel(BallotTestCase):

    def test_str_value(self):
        pp = ProposalFactory.create()
        self.assertEqual(pp.__str__(), pp.title)
        
    def test_allow_delete(self):
        pp = ProposalFactory.create()
        self.assertTrue(pp.allow_delete)

    def test_sort_order(self):
        pp1 = ProposalFactory.create(title='Alpha',sort_order=2)
        pp2 = ProposalFactory.create(title='Omega',sort_order=1)
        self.assertEqual(Proposal.objects.all()[0],pp2)

    def test_sort_order_2(self):
        pp3 = ProposalFactory.create(title='Alpha')
        pp4 = ProposalFactory.create(title='Omega')
        self.assertEqual(Proposal.objects.all()[0],pp3)

    def test_sort_order_3(self):
        ## NULL sorts before a sort_order value 
        pp5 = ProposalFactory.create(title='Alpha')
        pp6 = ProposalFactory.create(title='Omega',sort_order=1)
        self.assertEqual(Proposal.objects.all()[0],pp5)

