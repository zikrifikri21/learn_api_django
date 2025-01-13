from decouple import config
import requests
from rest_framework.views import APIView
from rest_framework.response import Response

# Get the API key from the environment variable
# API_KEY = config('API_KEY')

# Get the API secret from the environment variable
# API_SECRET = config('API_SECRET')

# Get the API URL from the environment variable
API_URL = config('API_URL')

class FaceRecognitionView(APIView):
    def post(self, request):
        # Get the image from the request
        image = request.data['image']

        # Send the image to the external API
        response = requests.post(API_URL, files={'image': image})

        # Check if the request was successful
        if response.status_code == 200:
            faces = response.json()
        else:
            faces = {'error': 'Failed to detect faces'}

        # Return the faces
        return Response(faces)