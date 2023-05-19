from rest_framework import serializers

from courses.models import Course

class CourseSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "name"]