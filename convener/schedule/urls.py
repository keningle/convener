from django.conf.urls import patterns, include, url
from rest_framework import routers
from schedule import views

router = routers.DefaultRouter()
router.register(r'presenters', views.PresenterViewSet)
router.register(r'locations', views.LocationViewSet)
router.register(r'tracks', views.TrackViewSet)
router.register(r'sessions', views.SessionViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)
