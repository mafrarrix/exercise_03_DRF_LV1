from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from jobBoardAPI.models import JobOffer
from jobBoardAPI.api.serializers import JobOfferSerializer

class JobOfferListCreateAPIview(APIView):
    
    def get(self, request):
        JobOffers = JobOffer.objects.filter(avabile=True)
        serializer = JobOfferSerializer(JobOffers, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = JobOfferSerializer(data=request)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class JobOfferDetailAPIview(APIView):
     
    def get_object(self, pk):
        JobOffer = self.get_object_or_404(JobOffer, pk=pk)
        return JobOffer
    
    def get(self, request, pk):
        JobOffer = self.get_object(pk)
        serilizer = JobOfferSerializer(JobOffer)
        return Response(serilizer.data)
    
    def put(self, request, pk):
        JobOffer = self.get_object(pk)
        erializer = JobOfferSerializer(JobOffer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        JobOffer = self.get_object(pk)
        JobOffer.delete
        return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)
     
    