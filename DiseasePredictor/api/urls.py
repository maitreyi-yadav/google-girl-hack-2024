from django.urls import path

from api.views.new_view import DoctorPredictionView

urlpatterns = [
    path("recommend-doc", view=DoctorPredictionView.as_view(), name="recommend-doc")
]
