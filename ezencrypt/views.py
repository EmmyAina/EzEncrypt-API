from rest_framework.views import APIView, Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .serializer import UploadSerializer
import subprocess


class EzEncryptAPI(APIView):
	parser_classes = [MultiPartParser, FormParser]

	def get(self,request):
		items = ["apple", "fruits", 'banana']
		result  = {"data": items}

		return Response(result, status=status.HTTP_200_OK)
	
	def post(self, request, *args, **kwargs):
		serialized_data = UploadSerializer(data=request.data)

		if serialized_data.is_valid():
			password = serialized_data.validated_data.get('password')
			algo = serialized_data.validated_data.get('algo')
			file_data = serialized_data.validated_data.get('file')

			try:
				read_data = file_data.read()
				print("File Data => ", read_data)
			except Exception as ex:
				print("Exception Error => ",ex)

			print(serialized_data.data)

			return Response(serialized_data.data, status=status.HTTP_201_CREATED)

		else:
			return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)



