from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from jobBoardAPI.models import JobOffer
from jobBoardAPI.api.serializers import JobOfferSerializer

class JobOfferListeCreateAPIview(APIView):
    
    def get(self,request):
        JobOffers = JobOffer.object.filter(active=True)
        serializer = JobOfferSerializer(JobOffer, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = JobOfferSerializer(data=request)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors), status=status.HTTP_400_BAD_REQUEST
    
 class JobOfferDetailAPIview(APIView):
     
     def get_object(self, pk)
        JobOffer = get_object_or_404(JobOffer, pk=pk)
        return JobOffer
    
     def get(self, request, pk):
          JobOffer = get_object(pk)
          serilizer = JobOfferSerializer(JobOffer)
          return Response(serilizer.data)
    
     #def put(self, request, pk):
        
     
    