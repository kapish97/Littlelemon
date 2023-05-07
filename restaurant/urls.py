from django.urls import path,include
from .views import bookingview,MenuitemView,BookingViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tables',BookingViewSet)

urlpatterns = [
    path('booking/',bookingview.as_view() ),
    path('menu',MenuitemView.as_view()),
    path('restaurant/booking/',include(router.urls)),
]
