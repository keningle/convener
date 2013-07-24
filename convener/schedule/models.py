from django.db import models

class Presenter(models.Model):
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    twitter = models.CharField(max_length=55, blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return self.name

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "name__icontains",)

class Location(models.Model):
    building = models.CharField(max_length=150)
    room = models.CharField(max_length=50)

    def __unicode__(self):
        return self.building + ' ' + self.room

class Track(models.Model):
    code = models.CharField(max_length=10)
    title = models.CharField(max_length=500)
    description = models.TextField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    def __unicode__(self):
        return self.title

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "title__icontains",)

class Session(models.Model):
    title = models.CharField(max_length=500, blank=True)
    description = models.TextField(blank=True, null=False)
    slides = models.URLField(blank=True, null=True)
    session_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    presenters = models.ManyToManyField(Presenter, blank=True, null=True)
    location = models.ForeignKey(Location, blank=True, null=True)
    tracks = models.ManyToManyField(Track, blank=True, null=True)

    def __unicode__(self):
        return self.title

    def get_presenters(self):
        # Returns a comma seperated list of presenters
        return ",".join([s.name for s in self.presenters.all()])
    get_presenters.short_description = 'Session Presenters'
