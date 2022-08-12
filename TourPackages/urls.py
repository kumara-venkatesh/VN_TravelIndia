from django.contrib import admin
from django.urls import path, re_path
from . import views

admin.site.site_header = 'Travel India - Administration'
admin.site.index_title = 'Travel India (Tours and Travel Management)'

urlpatterns = [
    path('', views.home, name='Home_URL' ), 
    path('packages/', views.packages, name='Package_URL' ),
    re_path(r'^packages_season/(?P<season>[\w-]+)', views.package_list.as_view(), name='Package_URL'),
    path('packages/<int:pk>/', views.package_details.as_view(), name='Package_details_URL'),
    path('about/', views.aboutus, name='AboutUs_URL' ),
    path('package_list/', views.package_list.as_view(), name='Package_List_URL' ),
    path('my_trips/', views.mytrip.as_view(), name='MyTrip_URL' ),
    path('my_trip/<int:pk>/', views.mytrip_details.as_view(), name='mytrip-detail'),
    path('rent_vehicle/', views.veh_rental, name='Veh_Rentals_URL' ),
]