from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from courses.models import Course
from courses.serializers import CourseSerialzier

class CourseAPI(APIView):
    # get all courses
    def get(self, *args, **kwargs):
        query = Course.objects.all()
        serializer = CourseSerialzier(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # create course
    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = CourseSerialzier(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    

class CourseDeleteAPI(APIView):
    def delete(self, request, pk=None, *args, **kwargs):
        instance = get_object_or_404(Course, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
