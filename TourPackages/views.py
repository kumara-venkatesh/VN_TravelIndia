from tkinter import messagebox
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def home(request):
    return render(request, 'TourPackages/Home.html')

def packages(request):
    return render(request, 'TourPackages/packages.html')

class package_details(DetailView):
    model = Packages
    template_name_suffix = '_details'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        

        if self.request.method == "GET":
            
            user = self.request.user
            book_trip = self.request.GET.get('applytrip')
            no_of_seats_requested = self.request.GET.get('no_of_seats')
            trasnport_opted = 'No' if self.request.GET.get('ntrans') else 'Yes'

            if book_trip:
                trip_for = Packages.objects.get(id=book_trip)
                if trasnport_opted == 'No':
                    trasnport_amount = getattr(trip_for,'Amount') - getattr(trip_for,'Amount')/100*20
                else:
                    trasnport_amount = getattr(trip_for,'Amount')
                
                trasnport_amount *= int(no_of_seats_requested)

                trip_available = TripInfo.objects.filter(Trip_For__PlaceName=trip_for,Trip_status="Planning")
                
                if trip_available:
                    trip_info = TripInfo.objects.get(Trip_For__PlaceName=trip_for,Trip_status="Planning")
                    available_seats = getattr(trip_info, 'Seats_Available')
                    
                    if int(no_of_seats_requested) > available_seats:
                        messages.warning(self.request,"%s seats are not available, Only %s seats are available"%(no_of_seats_requested,available_seats))
                    else:
                        booking = Trip_Requests.objects.create(Applied_By=user,Applied_For=trip_info,Transport_Opted=trasnport_opted,Payment_Status='Pending',No_of_Seats_Applied=no_of_seats_requested,Amount=trasnport_amount)
                        trip_info.Seats_Available = trip_info.Seats_Available - int(no_of_seats_requested)

                        booking.save()
                        trip_info.save()
                        messages.warning(self.request,"Your Booking Request is Successfully Submitted, Please pay %sRs under My Trips section"%trasnport_amount)

                else:
                    messages.warning(self.request,'Please Stay Tuned, Trip Schedule is not started, will notify to Travel India')

        return context
        
def aboutus(request):
    return render(request, 'TourPackages/about_us.html')

class package_list(ListView):
    model = Packages
    template_name = 'TourPackages/package_list.html'
    context_object_name = 'packag'
    
    def get_queryset(self):
        if 'season' in self.kwargs.keys():
            pack = Packages.objects.filter(Season=self.kwargs['season'])
        else:
            pack = Packages.objects.all()
        return pack
       
class mytrip(LoginRequiredMixin,ListView):
    model = Trip_Requests
    template_name = 'TourPackages/mytrip.html'
    context_object_name = 'requests'
    
    paginate_by = 5
    def get_queryset(self):
        req = Trip_Requests.objects.filter(Applied_By=self.request.user)
        return req

@login_required
def veh_rental(request):
    return render(request,'TourPackages/veh_rentals.html')
