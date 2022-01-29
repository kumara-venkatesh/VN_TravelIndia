from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    profilepic = models.ImageField(default = "Default.jpg", upload_to = 'Profile_Pics')
    dob = models.DateField()
    contact_no  = models.CharField(max_length=10)
    address = models.TextField(max_length=200)
    aadhar_no = models.CharField(max_length=12)

    def __str__(self):
        return self.user.first_name + '\'s Profile'

        
    


