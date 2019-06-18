'''
회원가입 기능을 하는    signup
로그인 기능을 하는      login
로그아웃 기능을 하는    logout
함수들을 가지고 있으며,

email_pattern 정규표현식을 통해 회원가입 및 로그인 시, 아이디를 검사합니다.

로그인, 로그아웃 및 회원가입 기능은 django의 auth기능 및 모델을 이용했으며, DB의 auth_user 테이블을 이용합니다.
'''

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

import re

email_pattern = re.compile(r'''
    #local part
    ^[a-zA-Z0-9]+       # 영문 대소문자 + 숫자는 1개 이상 으로 시작
    (
        [ _ \- [.] ]?   # '_', '-', '.' 은 사용 가능하지만 연속으로 2개 이상 올 수 없다.
        [a-zA-Z0-9]+    # 영문 대소문자 + 숫자  
    )*                  # 해당 패턴 반복 가능
    
    [@]                 # @은 반드시 1개 존재해야한다.

    #domain part
    [a-zA-Z0-9]+        # domain의 이름 부분
    (
        [ _ \- ]?       # '_', '-'은 사용 가능하지만 연속으로 2개 이상 올 수 없다.
        [a-zA-Z0-9]+    # 영문 대소문자 + 숫자  
    )*                  # 해당 패턴 반복 가능

    [.]                 # '.'은 반드시 1개는 존재해야 함
    [a-zA-Z0-9]+        # 영문 대소문자 + 숫자는 1개 이상

    (                   # 도메인이 .하나로 구분되지 않는 경우 ex) co.kr
        [.]?            # '.'
        [a-zA-Z0-9]+    # 영문 대소문자 + 숫자는 1개 이상
    )*
    $                   # 끝
''', re.VERBOSE)


def signup(request):
    '''
    회원가입 기능을 하는 함수입니다.
    
    POST로 받은 request의 경우, 에러의 경우 에러 메세지와 함께 signup 템플릿을 render하며
    에러가 아닌 경우, auth_user 테이블에 새로운 레코드를 추가(user생성)하며 로그인합니다.
    POST가 아닌 request의 경우, signup 템플릿을 render 해줍니다.
    (GET request = 메인 페이지에서 <a> 태그로 들어온 경우,
     POST request = signup 페이지에서 form을 제출한 경우)
    '''
    template_name = 'accounts/signup.html'

    if request.method == 'POST':
        input_id = request.POST['username']

        # 이메일 형태의 아이디가 아닌 경우
        if not email_pattern.match(input_id):
            return error_render(request, '이메일 형태의 아이디를 입력하세요', template_name)

        # 이미 해당 아이디가 있는 경우
        if User.objects.filter(username=input_id):
            return error_render(request, '해당 아이디는 이미 존재합니다', template_name)

        # 비밀번호 입력이 서로 일치하지 않는 경우
        if request.POST['password'] != request.POST['password-confirm']:
            return error_render(request, '비밀번호가 서로 일치하지 않습니다', template_name)

        # 회원가입이 성공적으로 이루어진 경우 (if 조건문은 추후 수정)
        if request.POST['password'] == request.POST['password-confirm']:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password']
            )
            auth.login(request, user)
            return redirect('base')

        # 알 수 없는 경우 다시 리로드
        return redirect('accounts:signup')

    return render(request, template_name)


def login(request):
    '''
    로그인 기능을 하는 함수입니다.

    GET request (<a>태그 혹은 url 입력)으로 들어온 경우, login.html 템플릿을 render해줍니다.
    POST request (accounts/login/ 에서 form을 제출)의 경우,
    ID가 이메일 형태가 아니면 에러 메세지와 함께 템플릿을 다시 render하고,
    auth.authenticate를 이용해 입력 받은 정보와 일치하는 유저를 찾고, 
    있다면 로그인 후 메인 페이지로 이동하고, 없으면 에러 메세지와 함께 템플릿을 다시 render합니다.
    '''
    template_name = 'accounts/login.html'

    if request.method == 'POST':
        input_id = request.POST['username']
        
        # 이메일 형태의 아이디가 아니면,        
        if not email_pattern.match(input_id):
            return error_render(request, '이메일 형태의 아이디를 입력하세요', template_name)

        # 비밀번호를 입력 받고 인증 시도
        input_pw = request.POST['password']
        user = auth.authenticate(request, username=input_id, password=input_pw)
        if user is not None:
            auth.login(request, user)
            return redirect('base')

        # 아이디, 비밀번호가 일치하지 않는 경우
        return error_render(request, '아이디 또는 비밀번호가 일치하지 않습니다', template_name)

    return render(request, template_name)


def logout(request):
    '''
    로그아웃 기능을 하는 함수입니다.

    메인페이지의 submit 버튼을 통해서만 POST request를 받고,
    POST request에 한해서만 logout이 되도록 했습니다.
    '''
    if request.method == "POST":
        auth.logout(request)
        return redirect('base')
    return redirect('base')


def error_render (request, error_m, template):
    '''
    request와 에러 메시지와 템플릿을를 받고, 
    boolean type의 is_error와 string type의 에러 메시지를 갖는 context를 형성하고,
    해당 request, 템플릿, context으로 render하는 함수입니다.

    View 함수가 아니라, 중복 코드를 없애기 위한 함수입니다.
    '''
    is_error = True
    context = {
        'is_error' : is_error,
        'error_m' : error_m
    }
    return render(request, template, context)
