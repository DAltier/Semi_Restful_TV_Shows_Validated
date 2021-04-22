from __future__ import unicode_literals
from django.db import models
from datetime import date, datetime

class ShowManager(models.Manager):
	def create_validator(self, postData):
		errors = {}
		if len(postData['title']) < 2:
				errors['title'] = "Title name should be at least 2 characters long"
		if Show.objects.filter(title = postData['title']).exists():
				errors['title'] = "This TV show already exists"
		if len(postData['network']) < 3:
				errors['network'] = "Network name should be at least 3 characters long"
		if len(postData['description']) < 10 and len(postData['description']) > 0:
				errors['desc'] = "The description should be at least 10 characters long"
		if len(postData['release_date']) == 0 or datetime.strptime(postData['release_date'], '%Y-%m-%d') > datetime.today():
				errors['release_date'] = "The release date should be a valid date and in the past"
		return errors


	def update_validator(self, postData):
		errors = {}
		if len(postData["title"]) < 2:
				errors["title"] = "Title must be at least 2 characters."
		if len(postData["network"]) < 3:
				errors["network"] = "Network must be at least 3 characters."
		if len(postData["description"]) < 10:
				errors["description"] = "Description must be at least 10 characters."
		if len(postData["release_date"]) > 0 and datetime.strptime(postData["release_date"], '%Y-%m-%d') > datetime.today() :
				errors["release_date"] = "Invalid release date."
		return errors


class Show(models.Model):
	title = models.CharField(max_length=255)
	network = models.CharField(max_length=255)
	release_date = models.DateTimeField()
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = ShowManager()

