from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .models import Direction
from .serializers import DirectionSerializers

# Create your views here.


class DirectionAPIView(APIView):

    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        print(request.data)
        try:
            file = request.data['image']
            request.data['image'] = file
        except KeyError:
            file = None
        serializer = DirectionSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        places = Direction.objects.all()
        serializer = DirectionSerializers(places, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DirectionAPIGetUpdateDeleteView(APIView):

    def get(self, request, id):
        place = Direction.objects.filter(id=id).first()
        if place is None:
            return Response({'error': 'Bad request'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = DirectionSerializers(Direction)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, id):
        place = Direction.objects.filter(id=id).first()
        if place is None:
            return Response({'error': 'Bad request'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = DirectionSerializers(
            Direction, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        direction = Direction.objects.filter(id=id).filter()
        if direction is None:
            return Response({'error': 'Bad request'}, status=status.HTTP_400_BAD_REQUEST)
        direction.delete()
        return Response({'mesage': 'lugar eliminado satisfactoriamente'}, status=status.HTTP_200_OK)
