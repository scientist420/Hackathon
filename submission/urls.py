from django.urls import path
from .views import HackathonList,SubmissionList,SubmissionDetails,custom_login

urlpatterns = [
    path('hackathons/', HackathonList.as_view(), name='hackathon-list-create'),
    
    path('submissions/', SubmissionList.as_view(), name='submission-list-create'),
    path('submissions/<int:pk>/', SubmissionDetails.as_view(), name='submission-detail'),
    path('login/',custom_login, name ='custom_login'),
]