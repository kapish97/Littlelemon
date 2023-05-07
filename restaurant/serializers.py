from rest_framework import serializers
from .models import Menu,Booking

class menuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class bookingSerializer(serializers.ModelSeriaizer):
    class Meta:
        model = Booking 
        fields = '__all__'