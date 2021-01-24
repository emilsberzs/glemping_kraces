from .models import Review
from django.forms import ModelForm


class ReviewForm(ModelForm):
    model = Review
    fields = ('name', 'body')
