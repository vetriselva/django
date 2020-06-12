from django.urls import path
from .views import estimate_id, EstimateViewSet
from rest_framework.routers import DefaultRouter 
router = DefaultRouter()
router.register('estimate', EstimateViewSet)
urlpatterns = [
	path('estimate_id/', estimate_id, name="estimate_id"),
]
urlpatterns += router.urls