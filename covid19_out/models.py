from django.db import models
from django.contrib.auth.models import User

class CovidChart(models.Model):
	country_affected = models.IntegerField()
	people_infected = models.IntegerField()
	death_people = models.IntegerField()
	overcomed_people = models.IntegerField()

	def __str__(self):
		return f"{self.country_affected}  {self.people_infected} {self.death_people} {self.overcomed_people} "


class Sugestion(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	subject = models.TextField(max_length=1000)

	def __str__(self):
		return f"{self.subject} from {self.user}"

class Questions(models.Model):
	question  = models.TextField()
	facteur = models.FloatField()

	def __str__(self):
		return self.question

class Diagnostic(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	question = models.ForeignKey(Questions, on_delete=models.CASCADE)
	oui = models.BooleanField(help_text='Oui', blank=True, default=False)
	non = models.BooleanField(help_text='Non', blank=True, default=False)

	def __str__(self):
		return f"{slef.user}-{self.question.question}-{self.oui}-{self.non}"



class BecomePartner(models.Model):
	firstname = models.CharField(max_length=60)
	lastname = models.CharField(max_length=60)
	residence = models.CharField(max_length=60)
	country = models.CharField(max_length=60)
	city =models.CharField(max_length=60)
	mail = models.EmailField()
	telephone = models.IntegerField()
	statut = models.CharField(max_length=100)
	description = models.CharField(max_length=100)
	avatar = models.ImageField(null=False, blank=False, upload_to="avatars/")

	def __str__(self):
		
		return f"{self.firstname} {self.lastname}"


class ContactUs(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	full_name = models.CharField(max_length=100)
	mail = models.EmailField()
	message = models.TextField()

	def __str__(self):
		return self.mail

