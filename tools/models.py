from django.db import models


class ToolType(models.Model):
	name = models.CharField(max_length=255, blank=False, null=False)

	def __str__(self):
		return self.name


class Tool(models.Model):
	name = models.CharField(max_length=255, blank=False, null=False)
	tool_type = models.ForeignKey(
		ToolType,
		on_delete=models.CASCADE
	)
	picture = models.ImageField(
		upload_to='tools/pictures',
		blank=True,
		null=True
	)

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name
