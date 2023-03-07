from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("yasin", views.yasin, name="yasin")
]