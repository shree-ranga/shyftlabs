from rest_framework import serializers

from results.models import Result

from students.serializers import StudentListSerializer
from courses.serializers import CourseSerialzier

class ResultListSerializer(serializers.ModelSerializer):
    student = StudentListSerializer()
    course = CourseSerialzier()

    class Meta:
        model = Result
        fields = ["id", "course", "student", "score"]


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = "__all__"