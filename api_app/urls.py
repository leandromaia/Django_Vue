from django.urls import path

from .views import PersonViews

urlpatterns = [
    path('person/', PersonViews.as_view())
]