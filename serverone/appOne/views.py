from .models import Sample
from appOne.serializers import ResponseSerializer
from .broker import process_stuff
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET'])
def SampleRouteForCelery(request):
    sample = Sample.objects.all()
    serializer_class = ResponseSerializer
    stuff = process_stuff()
    return Response({'processed': "From server-1", 'message': stuff.task_id})
    
@api_view(['GET'])
def SampleRoute(request):
    sample = Sample.objects.all()
    serializer_class = ResponseSerializer
    # stuff = process_stuff()
    return Response({'processed': "From server-1", 'message': "appOne"})
    



