from django.urls import path

from jobs.views import JobsDetailView

urlpatterns = [
    path("<int:pk>/", JobsDetailView.as_view(), name="job"),
]
