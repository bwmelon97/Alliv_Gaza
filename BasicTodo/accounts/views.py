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
    if request.method == 'POST':
        input_id = request.POST['username']
        
        # 이메일 형태의 아이디가 아닌 경우
        if not email_pattern.match(input_id):
            is_error = True
            error_message = '이메일 형태의 아이디를 입력하세요'
            context = {
                'is_error' : is_error,
                'error_m' : error_message 
            }
            return render(request, 'accounts/signup.html', context)

        # 비밀번호 입력이 서로 일치하지 않는 경우
        if request.POST['password'] != request.POST['password-confirm']:
            is_error = True
            error_message = '비밀번호가 서로 일치하지 않습니다'
            context = {
                'is_error' : is_error,
                'error_m' : error_message 
            }
            return render(request, 'accounts/signup.html', context)

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

    return render(request, 'accounts/signup.html')


def login(request):
    if request.method == 'POST':
        input_id = request.POST['username']
        
        # 이메일 형태의 아이디가 아니면,        
        if not email_pattern.match(input_id):
            is_error = True
            error_message = '이메일 형태의 아이디를 입력하세요'
            context = {
                'is_error' : is_error,
                'error_m' : error_message 
            }
            return render(request, 'accounts/login.html', context)

        input_pw = request.POST['password']
        user = auth.authenticate(request, username=input_id, password=input_pw)
        if user is not None:
            auth.login(request, user)
            return redirect('base')

        # 아이디, 비밀번호가 일치하지 않는 경우
        is_error = True
        error_message = '아이디 또는 비밀번호가 일치하지 않습니다'
        context = {
            'is_error' : is_error,
            'error_m' : error_message
        }
        return render(request, 'accounts/login.html', context)

    return render(request, 'accounts/login.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('base')
    return redirect('base')
