from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Packages)
admin.site.register(TripInfo)
admin.site.register(Trip_Requests)
admin.site.register(Rent_Vehicle)