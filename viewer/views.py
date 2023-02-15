from django.shortcuts import render, redirect
from viewer.models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

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

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Authenticate the user
            user = form.get_user()
            login(request, user)
            return redirect('reservation')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
