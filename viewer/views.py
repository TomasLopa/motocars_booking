from django.shortcuts import render, redirect
from .models import RaceTrack, Reservation, Event

def race_track_list(request):
    tracks = RaceTrack.objects.all()
    return render(request, 'race_track_list.html', {'tracks': tracks})

def reservation_list(request):
    reservations = Reservation.objects.all()
    return render(request, 'reservation_list.html', {'reservations': reservations})

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})
