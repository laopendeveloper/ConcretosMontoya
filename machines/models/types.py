from django.db import models


class Type(models.Model):

	name = models.CharField(max_length=50, blank=False, null=False)
	description = models.CharField(max_length=50, blank=False, null=False)

	def __str__(self):
		return self.name
