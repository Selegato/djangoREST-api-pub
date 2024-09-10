from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import CustomerViewSet, BenefitViewSet, CustomerBenefitViewSet
from .views import *

router = DefaultRouter()
router.register(r'customers', CustomerViewSet, basename='customers')
router.register(r'benefits', BenefitViewSet, basename='benefits')
router.register(r'customer-benefits', CustomerBenefitViewSet, basename='customer-benefits')

urlpatterns = [
    path('', include(router.urls)),
]