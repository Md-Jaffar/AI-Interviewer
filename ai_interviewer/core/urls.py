from django.urls import path
from .views import create_job, start_interview

urlpatterns = [
    path('create-job/', create_job),
    path('start-interview/', start_interview),
]