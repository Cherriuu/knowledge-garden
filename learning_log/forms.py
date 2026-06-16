from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm): # uses our topic model
    class Meta: # model form consists of a nested meta class
        model = Topic
        fields = ['text'] # only ask the user for text
        labels = {'text': ''} # removes Text: that normally shows up next to the input box

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text' : ''}
        widgets = {'text' : forms.Textarea(attrs={'cols' : 80})} # text area widget, modify to be 80 lines of text