from django.db import models

from students.models import Student
from courses.models import Course

class TrackingModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Result(TrackingModel):
    score_choices = (
    ("A", "A"),
    ("B", "B"),
    ("C", "C"),
    ("D", "D"),
    ("E", "E"),
    ("F", "F"),
    )
    student = models.ForeignKey(Student, related_name="results", on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name="results", on_delete=models.CASCADE)
    score = models.CharField(max_length=1, choices=score_choices)

