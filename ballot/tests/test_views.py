from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from ballot.tests.factories import (ElectionFactory, PrecinctFactory, RaceFactory,
									DistrictFactory, CandidateFactory, PartyFactory,
									OfficeFactory)
# from ballot.views import PrecinctBallotView



class BallotTestCase(TestCase):
	
	def setUp(self):
		# self.user1 = UserFactory.create(username='user1')
		# self.user1.set_password('!')
		# self.user1.save()
		# self.user2 = UserFactory.build(username='user2')
		# self.user2.set_password('!')
		# self.user2.save()        
		# self.user3 = UserFactory.build(username='user3')
		# self.user3.set_password('!')
		# self.user3.save()  

		self.e =  ElectionFactory.create()
		self.pr = PrecinctFactory.create()
		self.p = PartyFactory.create()
		self.d = DistrictFactory.create()
		self.d.precincts.add(self.pr)
		self.d.save()
		self.o = OfficeFactory.create(district=self.d)
		self.r = RaceFactory.create(office=self.o,election=self.e)
		self.c = CandidateFactory.create(race=self.r,party=self.p)


#### Testing the Views

class TestPrecinctListView(BallotTestCase):
	
	def setUp(self):        
		super(TestPrecinctListView,self).setUp()

	def test_successful(self):
		response = self.client.get(reverse('prec_list'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'ballot/precinct_list.html')
		self.assertEqual(response.context['object_list'].__len__(),1)
		self.assertContains(response,self.pr.__str__())

class TestPrecinctBallotView(BallotTestCase):
	
	def setUp(self):        
		super(TestPrecinctBallotView,self).setUp()
		
	def test_successful(self):
		response = self.client.get(reverse('prec_ballot', 
			kwargs = {'election_id': self.e.pk,'prec_id': self.pr.pk}))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'ballot/precinct_ballot.html')
		self.assertEqual(response.context['object_list'].__len__(),1)
		self.assertContains(response,self.c.name)


