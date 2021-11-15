from django import forms
from .models import Reservation


class DateTimeInput(forms.DateTimeInput):
    input_type = "datetime-local"


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        exclude = ['user', 'new', 'confirmation', 'email_text_one', 'email_text_two']
        widgets = {
            'datetime': DateTimeInput(),
        }


class DetailsForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'
