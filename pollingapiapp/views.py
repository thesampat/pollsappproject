from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serilizer import *
from .models import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.decorators import action

# Create your views here.

class UserViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = User.objects.all()
    serializer_class = UserSerilizer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request):
        queryset = UserProfile.objects.all()
        serializer = UserSerilizer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        data = request.data
        
        try:
            user= User.objects.filter(username=data['first_name']).get()
        except:
            user = User.objects.create_user(username=request.data['first_name'], password=request.data['password'], email=request.data['email'])

            
        data_change = {
            'User_C': user.pk,
            'Phone': request.data['Phone']
        }
        instance = UserSerilizer(data=data_change)
        if instance.is_valid():
            instance.save()
            return Response(instance.data)
        return Response(instance.errors)

class QuestionViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerilizers
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request):
        queryset = Question.objects.all()
        serializer = QuestionSerilizers(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        instance = QuestionSerilizers(data=request.data)
        if instance.is_valid():
            u = UserProfile.objects.filter(User_C=request.user).get()
            questions = Question.objects.filter(QUser=u)

            ## if limit reach 5 then return raise error
            if len(questions) == 5:
                return Response('You Have Reached Your Maximum Daily Limit Of Posting Questions')


            user = UserProfile.objects.get(User_C=request.user)
            instance.save(QUser=user)
            return Response(instance.data)
    
        return Response(instance.errors)
    
    @action(detail=True, methods=['GET'])
    def voteCount(self, request, pk=None):
        q = Question.objects.get(pk=pk)

        A = Vote.objects.filter(VQuestion=q).filter(Result='A').count()
        B = Vote.objects.filter(VQuestion=q).filter(Result='B').count()
        C = Vote.objects.filter(VQuestion=q).filter(Result='C').count()
        D = Vote.objects.filter(VQuestion=q).filter(Result='D').count()
        
        data = {
            "A":A,
            "B":B,
            "C":C,
            "D":D,
        }
        return Response(data)
    



class VotesViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Vote.objects.all()
    serializer_class = VoteSerilizer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request):
        queryset = Vote.objects.all()
        serializer = VoteSerilizer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        instance = VoteSerilizer(data=request.data)
        u = UserProfile.objects.filter(User_C=request.user).get()

        if instance.is_valid():
            try:
                votess = u.voted_by.all().filter(VQuestion=request.data['VQuestion'])
                print(votess)
                if len(votess) == 0:
                    instance.save(User=u)
                    return Response(instance.data)
                else:
                    return Response('You Already Voted For This Question')

            except:
                    pass
        
        return Response(instance.errors)
    
