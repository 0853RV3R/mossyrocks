# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from news.models import Story
from news.forms import StoryForm 
from django.contrib.auth.models import User 

def index(request):

	

	if request == "POST":
		print("Got form submission")
		form = StoryForm(request.POST)
		if form.is_valid:
			new_story = form.save()
			return redirect(index)

		else:
			print("Form has errors")
			response = 'Errors:'
			print("Else loop is called")
			form = StoryForm(request.POST)
			for key in form.errors.keys():
				value = form.errors[key]
				errors = ''
				for error in value:
					errors = errors + error + ' '
					response = response + ' ' + key + ': ' + errors
			return HttpResponse('<li class="error">' + response + '</li>')

	storyList = Story.objects.all().order_by('-date_posted')

	form = StoryForm()

	context = {
		'story': storyList,
		'form': form,

	}

	return render(request, 'news.html', context)

# def music(request):

# 	return

# def bio(request):

# 	return