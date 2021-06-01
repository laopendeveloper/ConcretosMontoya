	# Django
from django.db import models


class Machine(models.Model):

	name = models.CharField(max_length=70, blank=False, null=False)
	serial_number = models.CharField(max_length=255, blank=True, null=True)
	model = models.CharField(max_length=255, blank=True, null=True)
	description = models.TextField()
	price = models.FloatField()
	machine_type = models.ForeignKey('machines.Type', on_delete=models.CASCADE)
	is_available = models.BooleanField(default=True)
	rent_price = models.FloatField(default=0)

	photo = models.ImageField(
		upload_to='machines/pictures',
		blank=True,
		null=True
	)

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name
