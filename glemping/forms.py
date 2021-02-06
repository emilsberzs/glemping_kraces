from django.forms import ModelForm
from .models import Review, Reservation
from django import forms


class ReviewForm(ModelForm):
    RATING_CHOICES = (
        ('★☆☆☆☆', '★☆☆☆☆'),
        ('★★☆☆☆', '★★☆☆☆'),
        ('★★★☆☆', '★★★☆☆'),
        ('★★★★☆', '★★★★☆'),
        ('★★★★★', '★★★★★')
    )
    rating = forms.ChoiceField(
        choices=RATING_CHOICES, widget=forms.RadioSelect())

    class Meta:
        model = Review
        fields = ('rating', 'name', 'body')


class ReservationForm(ModelForm):

    class Meta:
        model = Reservation
        fields = ('name', 'surname', 'phone_number', 'email', 'date')
