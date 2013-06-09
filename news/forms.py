from django import forms
from django.forms import Textarea
from news.models import Story, Tourdate, Contact, Sounds

class StoryForm(forms.ModelForm):
        class Meta:
                model = Story
                widgets = {'message': Textarea(),}
                

class TourdateForm(forms.ModelForm):
        class Meta:
                model = Tourdate

class ContactForm(forms.ModelForm):
        class Meta:
                model = Contact

class SoundsForm(forms.ModelForm):
        class Meta:
                model = Sounds
