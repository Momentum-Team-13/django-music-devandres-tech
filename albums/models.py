from django.db import models


# Create your models here.
class Artist(models.Model):
	name = models.CharField(max_length=255)
	birthdate = models.DateField(null=True, blank=True)

	def __str__(self):
		return self.name


class Album(models.Model):
	title = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	artist = models.ManyToManyField(Artist)

	def __str__(self):
		return self.title

