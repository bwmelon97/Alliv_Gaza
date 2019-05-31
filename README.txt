기초적인 Todo 앱입니다 :)

.  
├── Alliv_Gaza.code-workspace               # vscode 워크스페이스 입니다.  
├── BasicTodo                             
│   ├── BasicTodo  
│   │   ├── __init__.py  
│   │   ├── settings.py                     # DB 서버는 저의 local mariadb 서버를 이용했습니다.
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── BasicTodo_nginx.conf                # 80번(기본)포트를 받아서 로컬 호스트의 9000번 포트의 gunicorn WSGI 서버를 이용하게 세팅되어 있습니다.
│   ├── accounts                            # 로그인 및 회원가입 기능을 다루는 앱입니다.
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── templates
│   │   │   └── accounts
│   │   │       ├── login.html
│   │   │       └── signup.html
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── gunicorn.conf.py                    # 로컬 호스트의 9000번 포트를 받습니다.
│   ├── manage.py
│   └── todo                                # todo 리스트를 생성,수정,삭제 할 수 있는 기능을 가진 앱입니다.
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── migrations
│       │   ├── 0001_initial.py
│       │   └── __init__.py
│       ├── models.py
│       ├── templates
│       │   └── todo
│       │       ├── index_login.html
│       │       └── index_not_login.html
│       ├── tests.py
│       ├── urls.py
│       └── views.py
├── Pipfile
└── Pipfile.lock

각 파이썬 파일들에 대한 자세한 설명은 해당 파일의 doc string을 확인해주세요 !
