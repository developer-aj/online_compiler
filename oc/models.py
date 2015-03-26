from django.db import models

class db(models.Model):
	code = models.TextField()
	inp = models.TextField(default="")
	out = models.TextField(default="")
