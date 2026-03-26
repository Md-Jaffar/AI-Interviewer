from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    company_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    skills = models.TextField()
    difficulty = models.CharField(max_length=50)

    def __str__(self):
        return self.role


class Interview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.job.role}"


class Response(models.Model):
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()
    score = models.IntegerField()
    feedback = models.TextField()

    def __str__(self):
        return self.question