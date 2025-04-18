from django.db import models

# Create your models here.

class Search(models.Model):
	search=models.CharField(max_length=500)
	created=models.DateTimeField(auto_now=True)

	def __str__(self):
		return f'{self.search}'

	class Meta:
		verbose_name_plural='searches'


class userreg(models.Model):
    username = models.CharField(max_length=20,null=True)
    email = models.CharField(max_length=20,null=True)
    password = models.CharField(max_length=20,null=True)
    