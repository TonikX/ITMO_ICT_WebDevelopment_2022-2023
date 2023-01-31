from django.urls import path
from .views import *

urlpatterns = [
    path('client/', ClientListAPIView.as_view()),
    path('client/create/', ClientCreateAPIView.as_view()),
    path('client/<int:pk>/', ClientRUDAPIView.as_view()),

    path('services/', ServicesPLListAPIView.as_view()),
    path('services/create/', ServicesPLCreateAPIView.as_view()),
    path('services/<int:pk>/', ServicesPLRUDAPIView.as_view()),

    path('materials/', MaterialsPLListAPIView.as_view()),
    path('materials/create/', MaterialsPLCreateAPIView.as_view()),
    path('materials/<int:pk>/', MaterialsPLRUDAPIView.as_view()),

    path('request/', RequestListAPIView.as_view()),
    path('request/create/', RequestCreateAPIView.as_view()),
    path('request/<int:pk>/', RequestRUDAPIView.as_view()),
    path('request/nested/', RequestNestedAPIView.as_view()),

    path('staff/', ExecutorListAPIView.as_view()),
    path('staff/create/', ExecutorCreateAPIView.as_view()),
    path('staff/<int:pk>/', ExecutorRUDAPIView.as_view()),

    path('chosenservices/', ChosenServicesListAPIView.as_view()),
    path('chosenservices/create/', ChosenServicesCreateAPIView.as_view()),
    path('chosenservices/<int:pk>/', ChosenServicesRUDAPIView.as_view()),
    path('chosenservices/full/', ChosenServicesFullListAPIView.as_view()),

    path('chosenmaterials/', ChosenMaterialsListAPIView.as_view()),
    path('chosenmaterials/create/', ChosenMaterialsCreateAPIView.as_view()),
    path('chosenmaterials/<int:pk>/', ChosenMaterialsRUDAPIView.as_view()),
    path('chosenmaterials/full/', ChosenMaterialsFullListAPIView.as_view()),

    path('workgroup/', WorkGroupListAPIView.as_view()),
    path('workgroup/create/', WorkGroupCreateAPIView.as_view()),
    path('workgroup/<int:pk>/', WorkGroupRUDAPIView.as_view()),
    path('workgroup/full/', WorkGroupFullListAPIView.as_view()),

    path('paymentorder/', PaymentOrderListAPIView.as_view()),
    path('paymentorder/create/', PaymentOrderCreateAPIView.as_view()),
    path('paymentorder/<int:pk>/', PaymentOrderRUDAPIView.as_view()),

]
