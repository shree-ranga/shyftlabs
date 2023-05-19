from django.db import models

class TrackingModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Student(TrackingModel):
    first_name = models.CharField(max_length=100)
    family_name = models.CharField(max_length=100)
    dob = models.DateField()
    email = models.EmailField()

    def __str__(self):
        return f"Student name: {self.first_name} {self.family_name}"
    