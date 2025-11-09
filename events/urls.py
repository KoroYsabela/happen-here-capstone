from . import views
from django.urls import path

urlpatterns = [
    path('', views.EventList.as_view(), name='home'),
    path('all_events/', views.AllEventsList.as_view(), name='all_events'),
    path('<slug:slug>/', views.event_detail, name='event_detail'),
    path('<slug:slug>/edit/', views.edit_event, name='edit_event'),
    path('<slug:slug>/book/', views.book_event, name='book_event'),
    path('<slug:slug>/delete/', views.delete_event, name='delete_event'),
    path('<slug:slug>/<int:booking_id>/cancel/', views.cancel_event, name='cancel_event'),
]
