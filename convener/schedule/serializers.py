from rest_framework import serializers
from schedule.models import Presenter, Location, Track, Session

class PresenterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Presenter
        fields = (
            'name', 
            'company',
            'bio',
            'twitter',
            'url',
            )

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = (
            'building',
            'room',
            )

class TrackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Track
        fields = (
            'code',
            'title',
            'description',
            'color',
            )

class SessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Session
        fields = (
            'title',
            'description',
            'slides',
            'session_date',
            'start_time',
            'end_time',
            'presenters',
            'location',
            'tracks',
            )