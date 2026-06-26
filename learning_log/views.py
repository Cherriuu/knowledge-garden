from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

def check_topic_owner(request, topic):
    if topic.owner != request.user:
        raise Http404
    
def check_entry_owner(request, entry):
    if entry.owner != request.user:
        raise Http404

# Create your views here.
def index(request): # request this
    return render(request, 'learning_log/index.html') # renders index.html on webpage

@login_required # requires for the user to be logged in to see this page, run this code first before topics
def topics(request):
    topics = Topic.objects.filter(owner=request.user).order_by('date_added') # stores a queryset in topics, a collection of data base objects
    context = {"topics":topics} # dictionary with key and value, key is how you write it on html and value is the actual data from your database
    return render(request, 'learning_log/topics.html', context)

@login_required
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id) # get the topic based off its topic id
    # -date_added sorts the entries in the reverse order that they were added

    check_topic_owner(request, topic)
    
    entries = topic.entry_set.order_by("-date_added") # from that topic, get the entry set (set of all entries associated with this topic)
    context = {"topic":topic, "entries":entries} # this is an example of a query because it queries the database for information
    # loads the html page for topic and injects the context (python object) into the html page
    return render(request, 'learning_log/topic.html', context) # always pass request as first parameter

@login_required
def new_topic(request):
    # add a new topic
    if request.method != 'POST': # if the user hasn't submitted the form, show them a blank one
        form = TopicForm() 
    else:
        # POST data was submitted, process the data
        form = TopicForm(request.POST) # request.POST is the data entered by the user
        if form.is_valid(): # django does this for us, checks if data is the correct specs
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_log:topics')) # redirect user to topic page, django looks for url by name so you dont hardcode the path
        
    context = {'form': form}
    return render(request, 'learning_log/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)

    check_topic_owner(request, topic)
    
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(request.POST) # fill the form with users input
        if form.is_valid(): # validate the form
            new_entry = form.save(commit=False) # build object, dont write to DB yet
            new_entry.topic = topic # attach the parent object
            new_entry.owner = request.user
            new_entry.save() # now save to database
            return HttpResponseRedirect(reverse('learning_log:topic', args=[topic_id]))
        
    context = {'topic' : topic, 'form' : form}
    return render(request, 'learning_log/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id) # find the entry based on the id
    topic = entry.topic # get the topic object that is tied with the entry

    check_entry_owner(request, entry)

    if request.method != 'POST': # if not submitted
        form = EntryForm(instance=entry) # fill the form with the users pre-existing entry
    else:
        form = EntryForm(instance=entry, data=request.POST) # pass users entry and new data entered by user
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_log:topic', args=[topic.id]))
        
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_log/edit_entry.html', context)

@login_required
def delete_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    check_entry_owner(request, entry)

    if request.method == 'POST': # yes, make changes to database
        entry.delete()
        return HttpResponseRedirect(reverse('learning_log:topic', args=[topic.id])) # redirect back to entry
    else:
        return HttpResponseRedirect(reverse('learning_log:topic', args=[topic.id]))
    # doesnt need render

@login_required
def delete_topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)

    check_topic_owner(request, topic)

    if request.method == 'POST':
        topic.delete()
        return HttpResponseRedirect(reverse('learning_log:topics'))
    else:
        return HttpResponseRedirect(reverse('learning_log:topics'))
