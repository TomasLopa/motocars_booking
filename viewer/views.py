from django.shortcuts import render, redirect, get_object_or_404
from viewer.models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ReservationForm
from .models import Reservation
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User



def racetrack(request):
    tracks = RaceTrack.objects.all()
    return render(request, 'racetrack.html', {'tracks': tracks})

def reservation(request):
    reservations = Reservation.objects.all()
    return render(request, 'reservations.html', {'reservations': reservations})


@login_required
def reservation_list(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'reservation_list.html', {'reservations': reservations})

def reservation_detail(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    return render(request, 'reservation_detail.html', {'reservation': reservation})

@login_required
def reservation_new(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            return redirect('reservation_list')
    else:
        form = ReservationForm()
    return render(request, 'reservation_new.html', {'form': form})


@login_required
def reservation_delete(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id, user=request.user)
    if request.method == 'POST':
        reservation.delete()
        return redirect('reservation_user')
    return render(request, 'reservation_confirm_delete.html', {'reservation': reservation})

@login_required
def reservation_user(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'reservation_user.html', {'reservations': reservations})


def events(request):
    events = Event.objects.get(id=1)
    context = {'events': events}
    return render(request, 'events.html', context)

def base(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'home.html')

