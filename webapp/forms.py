from django import forms
from .models import Tour

class TourForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = ['image', 'title', 'description']



from webapp.models import Tour
Tour.objects.all().values('title')

