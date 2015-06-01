from django.db import models

class db(models.Model):
	LANGUAGES = (
			('C', 'C'),
			('C++', 'C++'),
			('Python', 'Python'),
			('Ruby', 'Ruby'),
			('Java', 'Java'),
	)	

	code = models.TextField()
	inp = models.TextField(default="")
	out = models.TextField(default="")
	
	language = models.CharField(max_length=50, choices=LANGUAGES)

	def __str__(self):
		return self.language
