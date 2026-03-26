from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Job, Interview
from django.contrib.auth.models import User

@api_view(['POST'])
def create_job(request):
    print("DATA RECEIVED:", request.data)
    data = request.data
    job = Job.objects.create(
        company_name=data.get('company_name'),
        role=data.get('role'),
        skills=data.get('skills'),
        difficulty=data.get('difficulty')
    )
    return Response({"message": "Job created successfully"})


@api_view(['POST'])
def start_interview(request):
    user_id = request.data.get('user_id')
    job_id = request.data.get('job_id')

    try:
        user = User.objects.get(id=user_id)
        job = Job.objects.get(id=job_id)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=404)
    except Job.DoesNotExist:
        return Response({"error": "Job not found"}, status=404)

    interview = Interview.objects.create(user=user, job=job, score=0)

    return Response({
        "interview_id": interview.id,
        "user": user.username,
        "job": job.role,
        "message": "Interview started successfully"
    })