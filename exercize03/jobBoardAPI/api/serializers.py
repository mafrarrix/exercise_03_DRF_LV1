
from rest_framework import serializers
from jobBoardAPI.models import JobOffer
from datetime import datetime

class JobOfferSerializer(serializers.ModelSerializer):
    
    time = serializers.SerializerMethodField()
    
    class Meta:
        model = JobOffer
        exclude = ("id",)
        
    def time(self, object):
        publication_dete = object.create_at
        now = datetime.now()
        time_delta = timesince(publication_dete,now)
        return time_delta
        




# class JobOfferSerializer(serializers.Serializer()):
#     id = serializers.IntegerField(read_only=True)
#     company_name = serializers.CharField()
#     company_email = serializers.EmailField()
#     job_title = serializers.CharField()
#     job_description = serializers.CharField()
#     salary = serializers.IntegerField()
#     city = serializers.CharField()
#     state = serializers.CharField()
#     create_at = serializers.DateField(read_only=True)
#     avabile = serializers.BooleanField()