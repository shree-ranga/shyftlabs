from django.urls import path

from results.views import ResultAPI

urlpatterns = [
    path("", ResultAPI.as_view(), name="results")
]