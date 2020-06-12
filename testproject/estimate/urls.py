from django.urls import path
from .views import estimate,estimate_edit
urlpatterns = [
	path('estimate/', estimate, name= 'estimate'),
	path('estimate/<int:pk>/', estimate_edit, name= 'estimate_edit')
]