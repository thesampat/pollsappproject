from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import login as loginn
import requests
import json

# @login_required()
def home(request):
    messages.add_message(request, messages.INFO, 'Hello world.')

    print(request.user)

    x = requests.get('http://127.0.0.1:8000/api/questions/')
    questions = x.json()
    
    options = []
    votes= []
    for i in questions:
        ops = []
        ops.append(i['Op1'])
        ops.append(i['Op2'])
        ops.append(i['Op3'])
        ops.append(i['Op4'])
        options.append(ops)

        x = requests.get(f'http://127.0.0.1:8000/api/questions/{i["id"]}/voteCount/')        
        votes_data = x.json()
        vote = []
        vote.append(votes_data['A'])
        vote.append(votes_data['B'])
        vote.append(votes_data['C'])
        vote.append(votes_data['D'])
        votes.append(vote)
        

    questions = zip(questions, votes)
    return render(request, 'home.html', {'questions':questions, 'options': options, 'votes':votes})

def login(request):
    return render(request, 'login.html')

def profile(request):
    return render(request, 'profile.html')

def register(request):
    return render(request, 'register.html')

def createPoll(request):
    return render(request, 'createPoll.html')

def login_user(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    if user is not None:
        # A backend authenticated the credentials
        loginn(request, user)
        return redirect('home')
    else:
        # No backend authenticated the credentials
        return HttpResponse('no user found')

def register_user(request):
    return HttpResponse('how')

def logout_user(request):
    logout(request)
    return redirect('login')

def create_poll(request):
    data = request.POST
    question = data['question']
    a = data['op1']
    b = data['op2']
    c = data['op3']
    d = data['op4']

    data_json = {
        'question': question,
        'op1': a,
        'op2': b,
        'op3': c,
        'op4': d,
        'user': request.user
    }

    # headers = {'Content-type': 'application/json','Accept': 'text/plain'}
    r = requests.post('http://127.0.0.1:8000/api/questions/',data=data_json)

    print(r.json())

    return HttpResponse('creatint poll')


def register_user_api(request):
    data = request.POST    

    data_json = {
        'username' : data['Username'],
        'email' : data['Email'],
        'phone' : data['Phone'],
        'password': data['password'],}


    # # headers = {'Content-type': 'application/json','Accept': 'text/plain'}
    r = requests.post('http://127.0.0.1:8000/api/users/',data=data_json)

    print(r.json(), 'test, Check')

    return HttpResponse('creatint poll')
    
