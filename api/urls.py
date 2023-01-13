from django.urls import path
from . import views


urlpatterns = [
    path("", views.getRoutes, name="routes"),
    path("notes/", views.getNotes, name="notes"),
    path("notes/<int:pk>/", views.getNote, name="note")
]