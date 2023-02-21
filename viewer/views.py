from django.shortcuts import render, redirect
from viewer.models import *


def racetrack(request):
    tracks = RaceTrack.objects.all()
    return render(request, 'racetrack.html', {'tracks': tracks})

def reservation(request):
    reservations = Reservation.objects.all()
    return render(request, 'reservations.html', {'reservations': reservations})

def events(request):
    events = Event.objects.get(id=1)
    context = {'events': events}
    return render(request, 'events.html', context)

def base(request):
    return render(request, 'base.html')

