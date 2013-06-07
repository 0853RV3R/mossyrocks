from django import forms
from news.models import Story

class StoryForm(forms.ModelForm):

	class Meta:
		model = Story