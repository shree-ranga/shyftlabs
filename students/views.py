from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from students.models import Student
from students.serializers import StudentSerializer, StudentListSerializer

class StudentAPI(APIView):
    # create new student
    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = StudentSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    # get all students from the db
    def get(self, *args, **kwargs):
        query = Student.objects.all()
        serializer = StudentListSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class StudentDeleteAPI(APIView):
    # delete student
    def delete(self, request, pk=None, *args, **kwargs):
        instance = get_object_or_404(Student, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)