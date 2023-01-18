from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    User_C = models.OneToOneField(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=200, unique=True, null=True)
    Phone = models.SmallIntegerField()
    def __str__(self) -> str:
        return self.User_C.username
    
Vote_Choices = [
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
]

class Vote(models.Model):
    User = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='voted_by', null=True)
    VQuestion = models.ForeignKey('Question',on_delete=models.CASCADE, related_name='VQuestionr')
    Result = models.CharField(max_length=1, choices=Vote_Choices, default='A')

    def __str__(self) -> str:
        return self.Result


class Question(models.Model):
    QUser = models.ForeignKey(UserProfile, null=True, blank=True, on_delete=models.CASCADE, related_name='question_by')
    Question = models.CharField(max_length=300, unique=True, null=True)
    Op1 = models.CharField(max_length=100, null=True)
    Op2 = models.CharField(max_length=100, null=True)
    Op3 = models.CharField(max_length=100, null=True)
    Op4 = models.CharField(max_length=100, null=True)
    Date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.Question
    
   
    

