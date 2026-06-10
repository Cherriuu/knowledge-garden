from django.shortcuts import render
from .models import Topic

# Create your views here.
def index(request): # request this
    return render(request, 'learning_log/index.html') # renders index.html on webpage

def topics(request):
    topics = Topic.objects.order_by('date_added') # stores a queryset in topics, a collection of data base objects
    context = {"topics":topics} # dictionary with key and value, key is how you write it on html and value is the actual data from your database
    return render(request, 'learning_log/topics.html', context)

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id) # get the topic based off its topic id
    # -date_added sorts the entries in the reverse order that they were added
    entries = topic.entry_set.order_by("-date_added") # from that topic, get the entry set (set of all entries associated with this topic)
    context = {"topic":topic, "entries":entries} # this is an example of a query because it queries the database for information
    # loads the html page for topic and injects the context (python object) into the html page
    return render(request, 'learning_log/topic.html', context) # always pass request as first parameter