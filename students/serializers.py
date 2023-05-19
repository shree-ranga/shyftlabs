import datetime
from rest_framework import serializers
from rest_framework.validators import ValidationError

from students.models import Student

class StudentListSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ["id", "full_name", "dob", "email"]
        read_only_fields = ("id",)

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.family_name}"
    
class StudentSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = Student
        fields = "__all__"

    def validate(self, attrs):
        data = super().validate(attrs)
        if "dob" in data:
            today = datetime.date.today()
            if (today.year - data["dob"].year) < 10:
                raise ValidationError("Invalid dob. Student cannot be less than 10 years old")
        return data