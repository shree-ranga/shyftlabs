from django.urls import path


from students.views import StudentAPI, StudentDeleteAPI

urlpatterns = [
    path("", StudentAPI.as_view(), name="students"),
    path("<int:pk>", StudentDeleteAPI.as_view(), name="delete_student")
]