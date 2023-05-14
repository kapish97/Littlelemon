from django.urls import path,include
from .views import bookingview,MenuitemView,BookingViewSet,SingleItemView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'tables',BookingViewSet)

urlpatterns = [
    path('booking/',bookingview.as_view() ),
    path('menu',MenuitemView.as_view()),
    path('menu-items/<int:pk>/',SingleItemView.as_view()),
    path('restaurant/booking/',include(router.urls)),
    path('api-token-auth/',obtain_auth_token),
]
