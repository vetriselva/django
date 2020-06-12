from django.shortcuts import render
from django.http import HttpResponse
from .forms import EstimateForm
def estimate(request):
	form = EstimateForm()
	return render(request, 'manage_estimate.html', {'form':form})
def estimate_edit(request,pk):
	form = EstimateForm()
	return render(request, 'estimate_edit.html', {'form':form, 'id':pk})
