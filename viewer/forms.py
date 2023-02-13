from django import forms
from .models import *

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['date', 'status', 'number_of_seats', 'start_time', 'end_time']

class RaceTrackForm(forms.ModelForm):
    class Meta:
        model = RaceTrack
        fields = ['name', 'capacity', 'number_of_reservation']