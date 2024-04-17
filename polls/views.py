from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse

from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.http import JsonResponse
import json
from django.db.utils import OperationalError

from .models import Poll,Choice


def index(request):
    return render(request, 'login.html')


def home(request):
    poll_list = Poll.objects.all()
    return render(request, 'home.html', {'poll_list': poll_list}) 

def poll_detail(request, pollnum):
    poll = get_object_or_404(Poll, pk=pollnum)
    choices = Choice.objects.filter(pollId=pollnum)
    context={'poll':poll,'choices':choices}
    return render(request,'poll_detail.html',context)

def get_vote(request, votenum):
    
    return 0

def poll_result(request):
    poll= 0

def join(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        name = request.POST.get('name')

        # 사용자 이름이 이미 존재하는지 확인
        if User.objects.filter(username=id).exists():
            return JsonResponse({'success': False, 'message': '이미 사용 중인 아이디입니다.'})

        # 사용자 생성
        user = User.objects.create_user(username=id, password=pw, first_name=name)

        if user:
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'message': '계정 생성에 실패했습니다. 다시 시도해주세요.'})
    else:
        return render(request, 'join.html')    



@login_required
def poll_create(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            question = data.get('question')
            choices = data.get('choices', [])
            deadline = data.get('deadline')

            try:
                deadline = datetime.datetime.strptime(deadline, '%Y-%m-%d').date()
            except ValueError:
                error_message = '올바른 날짜 형식이 아닙니다.'
                return JsonResponse({'success': False, 'message': error_message})

            poll = Poll.objects.create(title=question, deadline=deadline)

            for choice_text in choices:
                poll.choice_set.create(choice_text=choice_text)

            return JsonResponse({'success': True})
        except OperationalError as e:
            return redirect('polls:home')  # 오류 발생 시 홈 페이지로 이동
        except Exception as e:
            return JsonResponse({'success': False, 'message': '투표 생성 중 오류가 발생했습니다.'})
    else:
        return render(request, 'poll_create.html')
    


    
def login(request):
    if request.method == 'POST':
        username = request.POST.get('id')
        password = request.POST.get('pw')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('polls:home')
        else:
            error_message = "아이디 또는 비밀번호를 확인해주세요."
            return render(request, 'login.html', {'error_message': error_message})
    return LoginView.as_view(template_name='login.html')(request)

def custom_logout(request):
    auth_logout(request)
    return redirect('polls:home')


def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return HttpResponseRedirect(request.GET.get('next', '/home/'))
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def poll_delete(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    poll.delete()
    return JsonResponse({'success': True})
