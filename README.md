# django-websocket
장고의 `channels`와 `channels-redis`를 활용하여 소켓 통신을 이용한 채팅 페이지 토이 프로젝트입니다.  
  
tags: `django`, `python`, `socket`  

# HOW TO RUN
이 프로그램은 Ubuntu 18.04 LTS 에서 진행되었습니다.  
하지만 동일한 방법으로 진행한다면, Windows 에서도 가능합니다.
   
```
git clone https://github.com/seovalue/django-websocket.git
cd django-websocket

#가상환경에서 실행하십시오.
pip install django==3.1.1
python -m pip install -U channels
python -m pip install -U channels-redis==2.1.4
```
  
django의 SECRET_KEY를 보호하기 위해 SECRET_KEY가 분리되도록 설정되어있습니다.  
따라서 django-websocket/secrets.json 를 생성한 뒤, 해당 secrets.json 파일에 다음과 같이 작성합니다.
```
{
	"SECRET_KEY" : "your_key"
}
```
your_key 부분에 생성한 장고 프로젝트의 settings.py 내 SECRET_KEY를 입력하면 실행할 수 있습니다.  
모든 설정이 완료된 후, 아래 명령어를 통해 실행할 수 있습니다. 
```
django-websocket/
python manage.py runserver
```

# HOW TO CONNECT
`python manage.py runserver`를 통해 서버를 실행시키면 `127.0.0.1:8000/chat` 을 통해 main page로 접속할 수 있습니다.  
메인 페이지에서 채팅방명을 입력하면 채팅방 내에서 채팅이 가능합니다.  
또한, chrome, firefox의 여러 탭을 이용해 접속한다면 같은 채팅방명으로 접속한 사용자끼리는 채팅 가능합니다.  

### contact
mathmjseo@khu.ac.kr
