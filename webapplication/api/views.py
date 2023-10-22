from rest_framework.response import Response

from rest_framework.decorators import api_view
from .serializers import MessageSerializer
from base.models import Message

@api_view(['GET'])
def getData(request):
    messages = Message.objects.all()
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def addData(request):
    serializer = MessageSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)