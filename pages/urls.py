from django.urls import path
from .views import HomePageView




urlpatterns = [
# path('appointments/', AppointmentsPageView.as_view(), name='appointments'),
path('', HomePageView.as_view(), name='home'),
]

