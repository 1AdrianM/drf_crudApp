from rest_framework import viewsets
from serializers import BookingSerializer
from .models import Bookings

class BookingViewSet(viewsets.ModelViewSet):
    queryset= Bookings.objects.all()
    serializer_class = BookingSerializer