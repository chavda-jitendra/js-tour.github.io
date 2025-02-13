from django.db import models

# Create your models here.
class Feedback(models.Model):
    id = models.AutoField(primary_key=True) 
    email = models.EmailField(max_length=255, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.email
    
class Tour(models.Model):
    image = models.ImageField(upload_to='tour_images/', blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class TourBooking(models.Model):
    fullname = models.CharField(max_length=255)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=20)
    selected_tour = models.CharField(max_length=255)
    preferred_travel_date = models.DateField()
    number_of_travelers = models.IntegerField()
    special_requests = models.TextField(blank=True, null=True)

    def __str__(self):
          return f'{self.fullname} - {self.selected_tour}'
    

