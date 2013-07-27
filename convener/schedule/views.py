from rest_framework import viewsets, permissions
from schedule.models import Presenter, Location, Track, Session
from schedule.serializers import (PresenterSerializer, LocationSerializer,
    TrackSerializer, SessionSerializer)

class PresenterViewSet(viewsets.ModelViewSet):
    '''
    API endpoint for Presenter
    '''
    queryset = Presenter.objects.all()
    serializer_class = PresenterSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class LocationViewSet(viewsets.ModelViewSet):
    '''
    API endpoint for Location
    '''
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class TrackViewSet(viewsets.ModelViewSet):
    '''
    API endpoint for Track
    '''
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class SessionViewSet(viewsets.ModelViewSet):
    '''
    API endpoint for Session
    '''
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)