from django.shortcuts import render, redirect, get_object_or_404
from datetime import date, datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout

from django.http import HttpResponseRedirect
from django.db.utils import IntegrityError

from .models import Poll,Choice,Vote
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import F
from django.contrib import messages
from .form import *

def index(request):
    return render(request, 'login.html')

def home(request):
    poll_list = Poll.objects.all()
    
    for poll in poll_list:
        count = 0
        for choice in poll.choice.all():
            count+=choice.count
        poll.total = count
        poll.save()

    context={'poll_list': poll_list}
    return render(request, 'home.html', context) 

def custom_login(request):
    if request.method == 'POST':
        id = request.POST['id']
        pw = request.POST['pw']
        user = authenticate(request, username=id, password=pw)
        if user is not None:
            auth_login(request,user)
            return redirect('polls:home')
        else:
            return render(request,'login.html', {'error': '아이디 비밀번호를 확인해주세요.'})
    else:
        return render(request,'login.html')   

def custom_logout(request):
    auth_logout(request)
    return redirect('polls:index')

def join(request):
    if request.method == 'POST':
        id = request.POST["id"]
        pw = request.POST["pw"]
        r_pw = request.POST["r_pw"]
        name = request.POST["name"]
        if User.objects.filter(username=id).exists():
            return render(request,'join.html', {'error': '이미 있는 아이디입니다.'})
        elif pw != r_pw:
            return render(request,'join.html', {'error': '패스워드가 일치하지 않습니다.'})
        elif User.objects.filter(first_name=name).exists():
            return render(request,'join.html', {'error': '이미 있는 이름입니다.'})
        
        try:
            User.objects.create_user(username=id, password=pw, first_name=name)
        except ValueError:
            return render(request,'join.html', {'error': '빈 필드가 있습니다.'})
        else:
            return redirect('polls:index')


           
    return render(request,'join.html')


def poll_detail(request, pollnum):
    poll = get_object_or_404(Poll, pk=pollnum)
    if poll.expireDate < date.today():
        messages.warning(request, '투표기한이 만료되었습니다. 결과보기를 눌러주세요')
        return redirect('polls:home')

    if Vote.objects.filter(poll=poll,voter=request.user).exists():
        messages.warning(request, '이미 투표하셨습니다. 다른투표를 선택해주세요')
        return redirect('polls:home')
    context={'poll':poll}
    return render(request,'poll_detail.html',context)

def vote(request, pollnum):
    poll = get_object_or_404(Poll, pk=pollnum)
    try:
        selected_choice = poll.choice.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'poll_detail.html', {'poll':poll, 'error_message' : '항목 선택 후 투표하세요!'})
    else:
        Vote.objects.create(poll=poll,choice=selected_choice,voter=request.user)
        selected_choice.count = F('count') + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:home'))

def poll_result(request, pollnum):
    poll = get_object_or_404(Poll, pk=pollnum)
    context={'poll':poll}
    return render(request,'poll_result.html',context)

@login_required
def poll_create(request):
    if request.method == 'POST':
        questionText = request.POST.get('question-field')
        pollImage = request.FILES.get('file')
        expireDate = request.POST.get('date')
        secretPoll = True
        if request.POST.get('options')=='2':
            secretPoll = False

        if datetime.strptime(expireDate,"%Y-%m-%d") < datetime.now():
            return render(request,'poll_create.html', {'error': '투표 만료일을 오늘보다 더 늦게 설정하세요.'})
        choice_count = 0 
        for i in range(12):
            if request.POST.get("{}".format(i+1)) == None:
              break
            else:
                choice_count+=1

        poll = Poll.objects.create(userId=request.user,
                        questionText=questionText,
                        pollImage=pollImage,
                        expireDate=expireDate,
                        secretPoll=secretPoll)

        for i in range(choice_count):
            poll.choice.create(choiceText=request.POST.get("{}".format(i+1)))

        return redirect('polls:home')
    else:
        return render(request, 'poll_create.html') 



                                    


    