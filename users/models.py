"""Users models."""

# Django
from django.contrib.auth.models import User
from django.db import models

# Utils
from utils.models import ConcretosModel


class Profile(models.Model):

	user = models.OneToOneField(
		User,
		on_delete=models.CASCADE
	)

	phone_number = models.CharField(max_length=20, blank=True)
	address = models.CharField(max_length=255, blank=True)

	picture = models.ImageField(
		upload_to='users/pictures',
		blank=True,
		null=True
	)

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.user.username
