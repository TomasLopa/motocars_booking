from django.shortcuts import render, redirect
from .forms import ReservationForm
from .forms import RaceTrackForm

def reservation_view(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.save()
            return redirect('reservation_success')
    else:
        form = ReservationForm()
    return render(request, 'reservation.html', {'form': form})

def create_racetrack(request):
    if request.method == 'POST':
        form = RaceTrackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('racetracks_list')
    else:
        form = RaceTrackForm()
    return render(request, 'create_racetrack.html', {'form': form})