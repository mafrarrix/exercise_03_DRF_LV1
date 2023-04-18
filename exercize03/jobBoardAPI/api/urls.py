from django.urls import path
from jobBoardAPI.api.views import JobOfferListCreateAPIview, JobOfferDetailAPIview

urlpatterns = [
    path('jobs/', JobOfferListCreateAPIview.as_view(), name='job-list'),
    path('jobs/<int:pk>', JobOfferDetailAPIview.as_view(), name='job-details')
    
]
