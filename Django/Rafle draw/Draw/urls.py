from django.urls import path
from .views import RaffleDrawView, AddParticipantView, ParticipantsView     

urlpatterns = [
    path('', RaffleDrawView.as_view(), name='raffle_draw'),
    path('add_participant/', AddParticipantView.as_view(), name='add_participant'),
    path('participants/', ParticipantsView.as_view(), name='participants'),
    ]
