from django.contrib import admin
from schedule.models import Presenter, Location, Track, Session

class LocationAdmin(admin.ModelAdmin):
    list_display = ('building', 'room')

class SessionAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_presenters', 'session_date')
    search_fields = ('title', 'presenters')
    raw_id_fields = ('presenters', 'tracks')
    autocomplete_lookup_fields = {
        'm2m': ['presenters', 'tracks'],
    }


admin.site.register(Presenter)
admin.site.register(Location, LocationAdmin)
admin.site.register(Track)
admin.site.register(Session, SessionAdmin)
