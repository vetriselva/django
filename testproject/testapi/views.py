from django.shortcuts import render
from rest_framework import generics,viewsets
from .models import Estimates
from .serializer import EstimateSerializer
from django.http import JsonResponse
class EstimateViewSet(viewsets.ModelViewSet):
	queryset = Estimates.objects.all()
	serializer_class = EstimateSerializer
def estimate_id(request):
	estimate = Estimates.objects.last()
	data = {"estimate_id": estimate.quote_number}
	return JsonResponse(data)


