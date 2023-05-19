from django.db import models

class TrackingModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Course(TrackingModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"Course name: {self.name}"
