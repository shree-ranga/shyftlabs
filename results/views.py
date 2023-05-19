from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from results.models import Result
from results.serializers import ResultSerializer, ResultListSerializer

class ResultAPI(APIView):
    # get all results
    def get(self, *args, **kwargs):
        query = Result.objects.all()
        serialzier = ResultListSerializer(query, many=True)
        return Response(serialzier.data, status=status.HTTP_200_OK)
    
    # create a result
    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = ResultSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
