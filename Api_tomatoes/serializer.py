from rest_framework import serializers
from .models import ImageData

class ImageSerializer(serializers.ModelSerializer):
	class Meta:
		model=ImageData
		fields=('pk','image','plantname')