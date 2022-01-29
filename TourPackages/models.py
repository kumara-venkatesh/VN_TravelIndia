from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
Seasons = (
    ("",""),
    ("Spring", "Spring"),
    ("Summer", "Summer"),
    ("Monsoon", "Monsoon"),
    ("Autumn", "Autumn"),
    ("Pre-Winter", "Pre-Winter"),
    ("Winter", "Winter"),
    
)
class Packages(models.Model):
    
    PlaceImage1 = models.ImageField(default = "DPlace.jpg", upload_to = 'Places/')
    PlaceImage2 = models.ImageField(default = "DPlace.jpg", upload_to = 'Places/')
    PlaceImage3 = models.ImageField(default = "DPlace.jpg", upload_to = 'Places/')
    PlaceName = models.CharField(max_length=100, default=None, null=True)
    Country = models.CharField(max_length=100, default=None, null=True)
    State = models.CharField(max_length=100, default=None, null=True)
    City = models.CharField(max_length=100, default=None, null=True)
    PlaceDescription = models.TextField(default=None, null=True)
    no_Days = models.CharField(max_length=10, default=None, null=True)
    Amount = models.CharField(max_length=10, default=None, null=True)
    stayDetails = models.TextField(default=None, null=True)
    Activities = models.TextField(default=None, null=True)
    Startpoint = models.CharField(max_length=50, default=None, null=True )
    Endpoint = models.CharField(max_length=50, default=None, null=True)
    Exclusions = models.TextField(default=None, null=True)
    Season = models.CharField(max_length=50, default=None, null=True, choices=Seasons)


    def __str__(self):
        return self.PlaceName

class TripInfo(models.Model):
    Seats_Available = models.CharField(max_length=5)
    Trip_Start_Date = models.DateTimeField()
    Trip_End_Date = models.DateTimeField()
    Trip_For = models.ForeignKey(Packages, on_delete=models.CASCADE)

class Trip_Requests(models.Model):
    Date_Applied = models.DateTimeField(default=timezone.now)
    Applied_By = models.ForeignKey(User, on_delete=models.CASCADE)
    Applied_For = models.ForeignKey(TripInfo, on_delete=models.CASCADE)
    Transport_Opted = models.CharField(max_length=20)
    Payment_Status = models.CharField(max_length=20)
    No_of_Seats_Applied = models.CharField(max_length=20)

    def __str__(self):
        return self.Applied_By
