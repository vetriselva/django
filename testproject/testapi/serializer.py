from rest_framework import serializers
from .models import Estimates

class EstimateSerializer(serializers.ModelSerializer):
	class Meta:
		model 	= Estimates
		fields 	= '__all__'
			