from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(r'passenger',Passenger_viewsets,basename = 'passenger')
router.register(r'review',Review_viewsets,basename = 'review')
router.register(r'user',User_viewsets,basename = 'user')
router.register(r'travel',Air_travel_viewsets,basename = 'travel')
router.register(r'airline',Airline_viewsets,basename = 'airline')
urlpatterns = router.urls