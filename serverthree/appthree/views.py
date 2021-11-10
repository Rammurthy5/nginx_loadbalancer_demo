from .models import Sample
from appthree.serializers import ResponseSerializer
from .helper import process_stuff
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def SampleRoute(request):
    sample = Sample.objects.all()
    print(sample)
    serializer_class = ResponseSerializer

    return Response({'processed': "From server-3", 'message': "appThree"})
    