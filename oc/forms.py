from django import forms
from .models import db

class PostForm(forms.ModelForm):
	class Meta:
		model = db
		fields = ('code','inp','language')
