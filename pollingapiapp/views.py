from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serilizer import *
from .models import *
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import SessionAuthentication, BasicAuthentication 
from django_celery_beat.models import PeriodicTask, IntervalSchedule

# executes every 10 seconds.
schedule, created = IntervalSchedule.objects.get_or_create(
    every=10,
    period=IntervalSchedule.SECONDS,
)


# Create your views here.

class UserViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = User.objects.all()
    serializer_class = UserSerilizer
    permission_classes = [AllowAny]

    def list(self, request):
        queryset = UserProfile.objects.all()
        serializer = UserSerilizer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        try:
            user_in = User.objects.filter(username=request.data['username']).get()
        except:
            user_in = User.objects.create_user(username=request.data['username'], password=request.data['password'], email=request.data['email'])

        real_data = {
            'User_C':user_in.pk,
            'Phone':request.data['phone']
        }

        inst = UserSerilizer(data=real_data)
        if inst.is_valid():
            inst.save()
            return Response('User Created')
        else:
            return Response(inst.errors)

class QuestionViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerilizers
    permission_classes = [AllowAny]

    def list(self, request):
        queryset = Question.objects.all()
        serializer = QuestionSerilizers(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):

        user_instance = request.data['user']
        
        data = {
            'Question':request.data['question'],
            'Op1':request.data['op1'],
            'Op2':request.data['op2'],
            'Op3':request.data['op3'],
            'Op4':request.data['op4'],
        }


        instance = QuestionSerilizers(data=data)
        if instance.is_valid():
            try:
                user_in = User.objects.filter(username=user_instance).get()
                u = UserProfile.objects.get(User_C=user_in.pk)
                questions = Question.objects.filter(QUser=u)
            except:
                return Response('error user')

        #     ## if limit reach 5 then return raise error
            if len(questions) == 5:
                return Response('You Have Reached Your Maximum Daily Limit Of Posting Questions')
            else:
                instance.save(QUser=u)
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
    


# @csrf_exempt
class VotesViewSet(ModelViewSet):

    authentication_classes = [BasicAuthentication]

    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Vote.objects.all()
    serializer_class = VoteSerilizer
    permission_classes = [AllowAny]

    def list(self, request):
        queryset = Vote.objects.all()
        serializer = VoteSerilizer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        user_instance = request.data['User']
        instance = VoteSerilizer(data=request.data)
        try:
            user_in = User.objects.filter(username=user_instance).get()
            u = UserProfile.objects.get(User_C=user_in.pk)
            print(u, 'check')
        except:
            print('sorry')
        
        print(request.data)

        if instance.is_valid():
            try:
                votess = u.voted_by.all().filter(VQuestion=request.data['VQuestion'])
                print(votess)
                if len(votess) == 0:
                    instance.save(User=u)
                    return Response(instance.data)
                else:
                    return Response({
                        'already':True
                    })

            except:
                    return Response('somethign went wrong')
        
        return Response(instance.errors)
    
