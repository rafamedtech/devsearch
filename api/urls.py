from api.views import getRoutes
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.getRoutes)
]