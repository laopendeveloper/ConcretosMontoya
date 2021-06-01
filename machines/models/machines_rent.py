from django.db import models


class Rent(models.Model):

	client = models.CharField(
		max_length=255,
		blank=False,
		null=False
	)
	
	machine = models.ForeignKey(
		'machines.Machine',
		on_delete=models.CASCADE
	)

	rent_from = models.DateTimeField(
		auto_now=False,
		auto_now_add=False,
		blank=False,
		null=False
	)

	rent_to = models.DateTimeField(
		auto_now=False,
		auto_now_add=False,
		blank=False,
		null=False
	)

	notes = models.TextField()

	def __str__(self):
		return self.client
