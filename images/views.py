import hashlib
import requests
from PIL import Image
import imagehash
from io import BytesIO
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import ImageHash
from .serializers import ImageHashSerializer

class CalculateHashView(APIView):
    def post(self, request):
        image_url = request.data.get('image_url')

        # Download the image
        try:
            response = requests.get(image_url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        # Calculate MD5 and pHash
        try:
            image = Image.open(BytesIO(response.content))
            md5_hash = hashlib.md5(response.content).hexdigest()
            phash = str(imagehash.phash(image))
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        # Save to database
        image_hash = ImageHash.objects.create(image_url=image_url, md5_hash=md5_hash, phash=phash)
        serializer = ImageHashSerializer(image_hash)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ImageHashListView(generics.ListCreateAPIView):
    queryset = ImageHash.objects.all()
    serializer_class = ImageHashSerializer

class ImageHashDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ImageHash.objects.all()
    serializer_class = ImageHashSerializer
