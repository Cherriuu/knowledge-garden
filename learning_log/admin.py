from django.contrib import admin
from learning_log.models import Topic
from learning_log.models import Entry

# Register your models here.
admin.site.register(Topic) # register the code you created to admin site
admin.site.register(Entry)
