from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
# Create your views here.

from .models import Booking,Menu
from .serializers import bookingSerializer, menuSerializer

from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView,DestroyAPIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
class bookingview(APIView):
    def get(self,request):
        items = Booking.objects.all()
        serializer = bookingSerializer(items,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer =  menuSerializer(data =request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","data":serializer.data})

class MenuitemView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    item = Menu.objects.all()
    serializer = menuSerializer()

class SingleItemView(RetrieveUpdateAPIView,DestroyAPIView):
    queryset = Menu.objects.all()
    seriailzer = menuSerializer()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['url','username','email','groups']

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer
    permission_classes = [IsAuthenticated]


# class UserViewSet(viewsets.ModelViewSet):
#    queryset = User.objects.all() 
#    serializer_class = UserSerializer
#    permission_classes = [IsAuthenticated] 