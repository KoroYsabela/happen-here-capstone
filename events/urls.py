#from django.urls import path
#from .views import home_page_view

from . import views
from django.urls import path

urlpatterns = [
    path('', views.EventList.as_view(), name='home'),
    path('<slug:slug>/', views.event_detail, name='event_detail'),
    path('<slug:slug>/book/', views.book_event, name='book_event'),
]
