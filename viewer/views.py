from django.shortcuts import render, redirect
from viewer.models import *

def race_track_list(request):
    tracks = RaceTrack.objects.all()
    return render(request, 'race_track_list.html', {'tracks': tracks})

def reservation_list(request):
    reservations = Reservation.objects.all()
    return render(request, 'reservation_list.html', {'reservations': reservations})

def events(request):
    events = Event.objects.get(id=1)
    context = {'events': events}
    return render(request, 'events.html', context)

def base(request):
    return render(request, 'base.html')
