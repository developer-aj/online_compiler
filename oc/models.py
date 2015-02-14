from django.db import models
from django.utils import timezone

# Create your models here.
class Portal(models.Model):
	user = models.ForeignKey('auth.User')
	code = models.TextField()
	compiled_at = models.DateTimeField(default=timezone.now)
