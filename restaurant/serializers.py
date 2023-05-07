from rest_framework.serializers import ModelSerializer
from .models import Menu,Booking

class menuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class bookingSerializer(ModelSerializer):
    class Meta:
        model = Booking 
        fields = '__all__'