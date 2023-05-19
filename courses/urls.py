from django.urls import path

from courses.views import CourseAPI, CourseDeleteAPI

urlpatterns = [
    path("", CourseAPI.as_view(), name="courses"),
    path("<int:pk>", CourseDeleteAPI.as_view(), name="delete_course")
]