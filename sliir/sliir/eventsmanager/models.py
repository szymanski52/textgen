from django.db import models
from django.contrib.auth.models import User


class PrivateGoal(models.Model):
    goalId = models.AutoField(primary_key=True)
    goalName = models.CharField(max_length=100)
    goalInitialDate = models.DateTimeField()
    goalDeadline = models.DateTimeField()
    goalPriority = models.IntegerField(default=1)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)


class Event(models.Model):
    eventId = models.AutoField(primary_key=True)
    eventName = models.CharField(max_length=100)
    eventInitialDate = models.DateTimeField()
    eventDeadline = models.DateTimeField()
    eventGoalId = models.ForeignKey('PrivateGoal', on_delete=models.CASCADE)
