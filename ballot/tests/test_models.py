
from django.test import TestCase    
from django.db import IntegrityError
from django.core.exceptions import ValidationError
#from datetime import date, time
from datetime import datetime, timedelta

    
from .factories import (PartyFactory, UnitLevelFactory, GovernmentalUnitFactory, MunicipalityFactory, ElectionFactory)

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

