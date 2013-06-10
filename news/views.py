# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from news.models import Story, Tourdate, Contact, Sounds
from news.forms import StoryForm, TourdateForm, ContactForm, SoundsForm
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

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

    soundsList = Sounds.objects.all()

    storyList= storyList[:5]

    form = StoryForm()

    form2 = TourdateForm()

    form3 = SoundsForm()

    context = {
            'story': storyList,
            'form': form,
            'form2': form2,
            'form3': form3,
            'tourdate': tourdateList,
            'contact': contactList,
            'soundsList': soundsList,


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
        

def addSounds(request):
    print("sound request")

    if request.method == "POST":
        form = SoundsForm(request.POST)
        if form.is_valid:
            new_sound = form.save()
            print("new sound saved")
            return redirect(index)
        else:
            print("errors")
            response = 'Errors: '
            for key in form.errors.keys():
                value = form.errors[key]
                errors = ''
                for error in value:
                    errors = errors + error + ' '
                    response = response + ' ' + key + ': ' + errors
            return HttpResponse('<li class="error">' + response + '</li>')

    

    return redirect(index)

def deleteSounds(request, sound_id):

    s = get_object_or_404(Sounds, pk=int(sound_id))
    s.delete()

    return redirect(index)

def deleteStory(request, story_id):

    s = get_object_or_404(Story, pk=int(story_id))
    s.delete()

    return redirect(index)

def deleteTourdate(request, tourdate_id):

    s = get_object_or_404(Tourdate, pk=int(tourdate_id))
    s.delete()

    return redirect(index)

def readMore(request, story_id):
    
    s = get_object_or_404(Story, pk=int(story_id))

    tourdateList = Tourdate.objects.all().order_by('-date')

    contactList = Contact.objects.get(pk=int(1))

    soundsList = Sounds.objects.all()

    context = {
        'storyMore': s,
        'tourdate': tourdateList,
        'contact': contactList,
        'soundsList': soundsList,
        }

    return render(request, 'readMore.html', context)
        
    
