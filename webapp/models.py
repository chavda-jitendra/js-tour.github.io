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
