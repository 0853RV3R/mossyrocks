# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from news.models import Story, Tourdate, Contact
from news.forms import StoryForm, TourdateForm, ContactForm
from django.contrib.auth.models import User 

def index(request):

    if request.method == "POST":
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

    tourdateList = Tourdate.objects.all().order_by('-date')

    contactList = Contact.objects.get(pk=int(1))


    form = StoryForm()

    form2 = TourdateForm()

    context = {
            'story': storyList,
            'form': form,
            'form2': form2,
            'tourdate': tourdateList,
            'contact': contactList,


    }

    return render(request, 'news.html', context)

def addtourdate(request):

    if request.method == "POST":
        form = TourdateForm(request.POST)
        if form.is_valid:
            new_date = form.save()
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
    return redirect(index)


def editcontact(request):
    
    instance = Contact.objects.get(pk=int(1))
    form = ContactForm(instance=instance)

    if request.method == "POST":
        form = ContactForm(request.POST, instance = instance)
        if form.is_valid:
            new_date = form.save()
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
        return redirect(index)

    storyList = Story.objects.all().order_by('-date_posted')

    tourdateList = Tourdate.objects.all().order_by('-date')

    contactList = Contact.objects.all()
    
    context = {
        'form3': form,
        'story': storyList,
        'tourdate': tourdateList,
        'contact': contactList,
    }

    return render(request, 'edit.html', context)
        
        
