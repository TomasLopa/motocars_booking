from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['date', 'start_time', 'end_time', 'race_track', 'num_of_seats']