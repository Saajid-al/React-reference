from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status # status codes
from .models import Job
from .serializer import JobSerializer

@api_view(['GET'])
def get_Jobs(request):
    jobs = Job.objects.all() #array of all cjobs
    serializedData = JobSerializer(jobs, many=True).data
    return Response(serializedData)

#what are seria lizers
@api_view(['POST'])
def create_Job(request):
    data = request.data
    serializer = JobSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
