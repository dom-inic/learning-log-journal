from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
	""" a topic the user if learning about"""
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User)

	def __str__(self):
		""" return a string representation of the model"""
		return self.text

class Entry(models.Model):
	""" information about what you learnt in regard with the topic"""
	topic = models.ForeignKey( Topic)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'entries'

	def __str__(self):
		""" return a string representation of the model"""
		return self.text[:50] + "..."