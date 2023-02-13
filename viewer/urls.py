from . import views

urlpatterns = [
    path('adresa/', views.create_racetrack(), name='create_racetrack'),
]
