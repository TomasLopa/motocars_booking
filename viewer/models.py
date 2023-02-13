from django.db import models

# Create your models here.

class RaceTrack(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()
    number_of_reservation = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Reservation(models.Model):
    PENDING = 'PENDING'
    CONFIRMED = 'CONFIRMED'
    CANCELLED = 'CANCELLED'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (CONFIRMED, 'Confirmed'),
        (CANCELLED, 'Cancelled'),
    ]
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    race_track = models.ForeignKey(RaceTrack, on_delete=models.CASCADE)
    num_of_places = models.PositiveSmallIntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)

    def __str__(self):
        return f"{self.user} - {self.race_track} ({self.date} {self.start_time}-{self.end_time})"

