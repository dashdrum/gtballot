from django.db import models

from snips.models import ModelBase

class Party(ModelBase):
	code = models.CharField(max_length=3,blank=False,null=False)
	name = models.CharField(max_length=100,blank=False,null=False)

	def __unicode__(self):
		return self.name

	@property
	def allow_delete(self):
		''' any candidates linked ? '''
		if len(Party.objects.get(id=self.id).candidate_set.all()) == 0 :
			return True
		else:
			return False

	class Meta:
		ordering = ["name"]
		permissions = (('view_party', "View Party"),)
		verbose_name_plural = "parties"
	
	class Admin:
		pass

class UnitLevel(ModelBase): # (Federal, State, City, Township, Village, School, etc.)
	name = models.CharField(max_length=100,blank=False,null=False)
	code = models.CharField(max_length=3,blank=False,null=False)

	def __unicode__(self):
		return self.name

	@property
	def allow_delete(self):
		''' any govt units linked ? '''
		if len(UnitLevel.objects.get(id=self.id).governmentalunit_set.all()) == 0 :
			return True
		else:
			return False

	class Meta:
		ordering = ["name"]
		permissions = (('view_level', "View Unit Level"),)
	
	class Admin:
		pass

class GovernmentalUnit(ModelBase):
	name = models.CharField(max_length=100,blank=False,null=False)
	unit_level = models.ForeignKey(UnitLevel,blank=False,null=False)

	def __unicode__(self):
		return self.name

	@property
	def allow_delete(self):
		''' any districts linked ? '''
		if len(GovernmentalUnit.objects.get(id=self.id).district_set.all()) == 0 :
			return True
		else:
			return False

	class Meta:
		ordering = ["name"]
		permissions = (('view_unit', "View Governmental Unit"),)
	
	class Admin:
		pass

class Municipality(ModelBase): # (Name of a precinct)
	name = models.CharField(max_length=100,blank=False,null=False)
	code = models.CharField(max_length=3,blank=False,null=False)

	def __unicode__(self):
		return self.name

	@property
	def allow_delete(self):
		''' any Precincts linked ? '''
		if len(Municipality.objects.get(id=self.id).precinct_set.all()) == 0 :
			return True
		else:
			return False

	class Meta:
		ordering = ["name"]
		permissions = (('view_muni', "View Municipality"),)
		verbose_name_plural = "Municipalities"
	
	class Admin:
		pass

##----------------------------------------------------------------------------##	

class Election(ModelBase):
	name = models.CharField(max_length=100,blank=False,null=False)
	election_date = models.DateField(blank=False,null=False)

	def __unicode__(self):
		return self.name

	@property
	def allow_delete(self):
		''' any races or proposals linked ? '''
		if len(Election.objects.get(id=self.id).race_set.all()) == 0 and len(Election.objects.get(id=self.id).proposal_set.all()) == 0 :
			return True
		else:
			return False

	class Meta:
		ordering = ["election_date"]
		permissions = (('view_election', "View Election"),)
	
	class Admin:
		pass

class Precinct(ModelBase):
	municipality = models.ForeignKey(Municipality,blank=False,null=False)
	prec_number = models.CharField(max_length=2,blank=False,null=False)
	polling_location = models.CharField(max_length=100,blank=False,null=False)

	def __unicode__(self):
		return self.municipality.code + ' ' + self.prec_number

	@property
	def allow_delete(self):
		''' any districts linked ? '''
		if len(Precinct.objects.get(id=self.id).district_set.all()) == 0 :
			return True
		else:
			return False

	class Meta:
		ordering = ["municipality","prec_number"]
		permissions = (('view_precinct', "View Precinct"),)
	
	class Admin:
		pass

class District(ModelBase):
	name = models.CharField(max_length=100,blank=False,null=False)
	govt_unit  = models.ForeignKey(GovernmentalUnit,blank=False,null=False)
	precints = models.ManyToManyField(Precinct)

	def __unicode__(self):
		return self.name

	@property
	def allow_delete(self):
		''' any offices or proposals linked ? '''
		if len(District.objects.get(id=self.id).office_set.all()) == 0 and len(District.objects.get(id=self.id).proposal_set.all()) == 0 :
			return True
		else:
			return False

	class Meta:
		ordering = ["govt_unit","name"]
		permissions = (('view_district', "View District"),)
	
	class Admin:
		pass

class Office(ModelBase):
	district = models.ForeignKey(District,blank=False,null=False)
	name  = models.CharField(max_length=100,blank=False,null=False)

	def __unicode__(self):
		return self.district.__unicode__() + ' ' + self.name

	@property
	def allow_delete(self):
		''' any races linked ? '''
		if len(Office.objects.get(id=self.id).race_set.all()) == 0 :
			return True
		else:
			return False

	class Meta:
		ordering = ["district","name"]
		permissions = (('view_office', "View Office"),)
	
	class Admin:
		pass

class Race(ModelBase):
	votes_allowed = models.IntegerField(blank=False,null=False,default=1)
	election = models.ForeignKey(Election,blank=False,null=False)
	office = models.ForeignKey(Office,blank=False,null=False)

	def __unicode__(self):
		return self.election.__unicode__() + ' ' + self.office.__unicode__()

	@property
	def allow_delete(self):
		''' any candidates linked ? '''
		if len(Race.objects.get(id=self.id).candidate_set.all()) == 0 :
			return True
		else:
			return False

	class Meta:
		ordering = ["election","office"]
		permissions = (('view_race', "View Race"),)
	
	class Admin:
		pass

class Candidate(ModelBase):
	race = models.ForeignKey(Race,blank=False,null=False)
	name  = models.CharField(max_length=100,blank=False,null=False)
	ticket_mate  = models.CharField(max_length=100,blank=True,null=True) # (Lt. Gov, Vice Prez)
	party = models.ForeignKey(Party,blank=False,null=False)
	incumbent = models.BooleanField(blank=False,null=False,default=False)
	url = models.URLField(blank=True,null=True)

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ["name"]
		permissions = (('view_candidate', "View Candidate"),)
	
	class Admin:
		pass

class Proposal(ModelBase):
	district = models.ForeignKey(District,blank=False,null=False)
	election = models.ForeignKey(Election,blank=False,null=False)
	title = models.CharField(max_length=200,blank=False,null=False)
	text = models.TextField(blank=False,null=False)

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ["title"]
		permissions = (('view_proposal', "View Proposal"),)
	
	class Admin:
		pass

