from django.urls import path

from . import views

urlpatterns = [
    path("", views.PhonesView.as_view(), name='home'),
    path("search/", views.Search.as_view(), name='search'),
]
