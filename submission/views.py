from rest_framework import generics,permissions
from .models import Hackathon, Submission
from .serializer import HackathonSerializer,SubmissionSerializer
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


class HackathonList(generics.ListCreateAPIView):
    queryset = Hackathon.objects.all()
    serializer_class  = HackathonSerializer
    permission_class = [permissions.IsAuthenticated]

    def perform_create(self,serializer):
        serializer.save(created_by=self.request.user)

class SubmissionList(generics.ListCreateAPIView):
    query_set = Submission.objects.all()
    serializer_class = SubmissionSerializer
    permission_class = [permissions.IsAuthenticated]

    def perform_create(self,serializer):
        serializer.save(user=self.request)

class SubmissionDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    permission_class = [permissions.IsAuthenticated]  


@api_view(['POST'])
def custom_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username = username,password= password)
    if user is not None:
        login(request,user)
        return Response({'message ':"Login succesfull"},status=status.HTTP_200_OK)
    else:
        login(request,user)
        return Response({'message':"Uesrname or password is invalid"},status=status.HTTP_400_BAD_REQUEST)
    



