from . import views
from django.urls import path

urlpatterns = [
    path('', views.myevents_page, name='myevents'),
]