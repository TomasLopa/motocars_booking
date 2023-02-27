from django.shortcuts import render, redirect
from viewer.models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ReservationForm
from .models import Reservation, Event



def racetrack(request):
    tracks = RaceTrack.objects.all()
    return render(request, 'racetrack.html', {'tracks': tracks})

def reservation(request):
    reservations = Reservation.objects.all()
    return render(request, 'reservations.html', {'reservations': reservations})

@login_required
def create_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            messages.success(request, 'Rezervácia úspešne vytvorená!')
            return redirect('reservation_detail', pk=reservation.pk)
    else:
        form = ReservationForm()
    return render(request, 'create_reservation.html', {'form': form})


def reservation_list(request):
    reservations = Reservation.objects.all()
    return render(request, 'reservation_list.html', {'reservation_list': reservations})

def reservation_detail(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    return render(request, 'reservation_detail.html', {'reservation': reservation})


def events(request):
    events = Event.objects.get(id=1)
    context = {'events': events}
    return render(request, 'events.html', context)

def gallery(request):
    events = Event.objects.all()
    return render(request, 'gallery.html', {'events': events})


def base(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'home.html')


