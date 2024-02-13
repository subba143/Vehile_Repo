"""
URL configuration for Test_Proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Vehicle_App import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('v_list/', views.VehicleListAPIView.as_view()),
]


# Model: SUV
# Year: 2023
# Color: Red
# Mileage: 20,000 miles
# Vehicle type: Electric
# Seats: 70
# Vehicle seat type: Leather
# Owner: Single owner
#
# O contact: 8106093109




