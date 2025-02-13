from django.contrib import admin
from .models import Feedback
from .models import Tour
from .models import TourBooking

admin.site.register(Feedback)
admin.site.register(Tour)
admin.site.register(TourBooking)
# class TourBookingAdmin(admin.ModelAdmin):
#     list_display = ('fullname', 'email', 'phonenumber', 'selected_tour', 'preferred_travel_date', 'number_of_travelers')
