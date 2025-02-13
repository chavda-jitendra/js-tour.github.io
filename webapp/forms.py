from django import forms
from .models import Tour

class TourForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = ['image', 'title', 'description']


from webapp.models import Tour
Tour.objects.all().values('title')


from .models import TourBooking
class TourBookingForm(forms.ModelForm):
    class Meta:
        model = TourBooking
        fields = ['fullname', 'email', 'phonenumber', 'selected_tour', 'preferred_travel_date', 'number_of_travelers', 'special_requests']


