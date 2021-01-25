from django.forms import ModelForm
from .models import Review, Reservation


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ('name', 'body')


class ReservationForm(ModelForm):

    class Meta:
        model = Reservation
        fields = ('name', 'surname', 'phone_number', 'email', 'date',)
