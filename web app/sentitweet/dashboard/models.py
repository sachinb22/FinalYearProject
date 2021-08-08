from django.db import models
from datetime import datetime
# Create your models here.
class Dashboard(models.Model):
	title = models.CharField(max_length=20)
	tweets = models.IntegerField()
	date = models.DateTimeField(default=datetime.now, blank=True)
	description = models.TextField(blank=True)

	def __str__(self):
		return self.title