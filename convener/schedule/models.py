from django.db import models

class Presenter(models.Model):
    class Meta:
        verbose_name = _('Presenter')
        verbose_name_plural = _('Presenters')

    def __unicode__(self):
        pass

class Location(models.Model):
    class Meta:
        verbose_name = _('Location')
        verbose_name_plural = _('Locations')

    def __unicode__(self):
        pass

class Track(models.Model):
    code = models.CharField(max_length=10)
    title = models.CharField(max_length=500)
    description = models.TextField(required=False, null=True)
    color = models.CharField(max_length=10, required=False, null=True)

    class Meta:
        verbose_name = _('Track')
        verbose_name_plural = _('Tracks')

    def __unicode__(self):
        return self.title

class Session(models.Model):
    title = models.CharField(max_length=500, required=True)
    description = models.TextField(required=False, null=False)
    slides = models.URLField(required=False, null=True)
    session_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    presenters = models.ManyToManyField('Presenter', required=False, null=True)
    location = models.ForeignKey('Location', required=False, null=True)
    tracks = models.ManyToManyField('Track', required=False, null=True)

    class Meta:
        verbose_name = _('Presentation')
        verbose_name_plural = _('Presentations')

    def __unicode__(self):
        return self.title
    
