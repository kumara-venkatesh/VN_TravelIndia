from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Packages
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
        userinfo = self.request.user
        UserName = userinfo.first_name + ' ' + userinfo.last_name
        tripid = self.request.GET.get('applytrip')
        if self.request.method == "GET":
            pass
        return context
        
def aboutus(request):
    return render(request, 'TourPackages/about_us.html')

class package_list(ListView):
    model = Packages
    template_name = 'TourPackages/package_list.html'
    context_object_name = 'packag'
    
    paginate_by = 5
    def get_queryset(self):
        if 'season' in self.kwargs.keys():
            pack = Packages.objects.filter(Season=self.kwargs['season'])
        else:
            pack = Packages.objects.all()
        return pack
       
class mytrip(LoginRequiredMixin,ListView):
    model = Packages
    template_name = 'TourPackages/mytrip.html'
    context_object_name = 'packag'
    
    paginate_by = 5
    def get_queryset(self):
        pack = Packages.objects.all()
        return pack

@login_required
def veh_rental(request):
    return render(request,'TourPackages/veh_rentals.html')
