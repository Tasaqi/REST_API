from django.shortcuts import render
from rest_framework import viewsets
from .models import ImageData
from .serializer import ImageSerializer
from rest_framework import status
from rest_framework.response import Response
# Create your views here.

class ImageDataView(viewsets.ModelViewSet):
	queryset=ImageData.objects.all()
	serializer_class=ImageSerializer

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)

		if not serializer.is_valid(raise_exception=False):
			return Response({"Fail": "blablal"}, status=status.HTTP_400_BAD_REQUEST)
		self.perform_create(serializer) # ? 
		
		image=request.data['image']
		plantnameX=request.data['plantname']
		if plantnameX=="tomatoes":
			result=Cnn_model(image)
		else:
			result=""
		headers = self.get_success_headers(serializer.data)
		return Response({"Result": result},status=status.HTTP_201_CREATED ,headers=headers)


#Emmbeded Model
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
def Cnn_model(path):
		model= load_model("static/Api_tomatoes/90acc.model")
		test_image = image.load_img(path, target_size = (64, 64)) 
		test_image = image.img_to_array(test_image)
		test_image = np.expand_dims(test_image, axis = 0)
		test_image=test_image/255.0  
		#predict the result
		result = model.predict(test_image)
		print(result[0])
		index=0
		return  result[0]