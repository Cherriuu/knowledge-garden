from django.db import models

# Create your models here.
# Creates a database table with 3 columns: id (automatic unique number), text (user input, max 200 characters), and date_added (timestamp, auto-set on creation).
class Topic(models.Model):
    text = models.CharField(max_length = 200) # store a small amount of text
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
    
class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) # links two models together, every Entry belongs to one Topic
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries' # now multiple instances of this whole model will be called entries, not entry, helps django out with naming

    def __str__(self):
        return self.text[:50] + "..." # django handles self for you in the background

