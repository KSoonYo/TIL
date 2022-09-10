# WSGI for detail



## 1. WSGI의 등장 배경

### 3계층 시스템과 CGI

3계층 서버 시스템에 대해 들어본 적 있을 것이다. DB 서버는 차치하고 웹 서버와 어플리케이션 서버만 살펴보자. 초기에는 웹 서버만 있었다. 하드웨어에 파일과 이미지를 저장해두었다가 클라이언트로부터 요청이 들어오면 요청한 파일을 화면에 띄워주는 형식이었다.

이런 방식은 빠르고 편했지만 Only Static, 정적인 파일밖에 건네줄 수가 없었다. 그런데 클라이언트로부터 오는 요청이 다양하고 복잡해지면서 로직으로 구현해야 하는 동적인 파일에 대한 요청이 생겨나게 되고, 이런 정적인 파일만으로는 한계를 느끼게 되었다.

그래서 등장한 게 **웹 어플리케이션 서버**이다. 데이터 파일을 저장해두는 대신, 소스 스크립트를 서버에 저장해놓고 요청이 올 때마다 스크립트를 실행시켜 결과를 반환해주는 것이다. 쉽게 말해 소스 스크립트가 있는 웹 앱 자체를 클라이언트의 요청을 받는 웹 서버로 사용하는 것이다.

그런데, 여기서 **파이썬 스크립트가 어떻게 HTTP 요청을 받을 것인가**, 하는 문제가 발생한다.

HTTP 요청은 기본적으로 `GET /home.html HTTP/1.1` 과 같은 텍스트이고, 이는 파이썬 앱이 받는 request object의 형식과는 다르기 때문이다.

그래서 클라이언트로부터 오는 HTTP 요청을 파이썬 스크립트가 요구하는 데이터 형식으로 변환하고 응답을 돌려줄 때도 파이썬 데이터를 HTTP 형식으로 바꿔주는 작업이 필요한데, 이 때 파이썬 앱 서버가 동작하는 기본적인 방식이 **CGI, Common Gateway Interface**이다.

즉, CGI란 파이썬 어플리케이션 서버의 동작 방식에 대한 specification(사양, 매뉴얼)이라고 할 수 있고 그 기본적인 동작 과정은 다음과 같다.

- 인풋으로 HTTP 요청을 받는다.
- 요청에 대한 정보를 환경변수의 형식으로 만들어서 파이썬 스크립트의 stdin 형식의 인풋으로 받는다.
- 스크립트가 print와 같은 stdout 형식으로 응답하면 HTTP 형식으로 변환된다.

### WSGI의 등장

그런데 CGI는 한 가지 문제점이 있었는데, 바로 요청이 들어올 때마다 파이썬 스크립트를 처음부터 실행한다는 것이었다. 이렇게 되면 서버가 너무 느리고 효율도 좋지 않았다.

이 때 등장한 게 **WSGI(Web Server Gateway Interface)**이다. CGI처럼 WSGI 또한 웹 어플리케이션 서버의 동작 방식에 대한 specification인데, 기본적인 아이디어는 다음과 같다.

웹 서버와 파이썬 스크립트를 분리하고 웹 서버가 클라이언트의 요청을 받아서 스크립트에 전달해주면 스크립트는 스크립트 전체를 실행시키는 게 아니라 필요한 로직 하나만 실행한 후 결과를 응답해주는 식으로 동작함으로써 동적인 콘텐츠에 대한 요청에 빠르게 응답할 수 있게 한 것이다.

이러한 WSGI가 표준적인 파이썬 어플리케이션 서버의 동작 방식이 됨에 따라, WSGI 서버가 클라이언트의 요청을 받는 웹 서버의 역할을 하게 되고 WSGI compatible한 파이썬 앱이 WSGI 서버와 합쳐져서 웹 어플리케이션 서버가 되게 된다.
![img](https://media.vlpt.us/images/jimin_lee/post/19d94186-29f9-4cf2-a9c3-0b9e7bb39086/KakaoTalk_20210425_212448657_01.jpg)

즉, 여기서 WSGI 서버의 역할을 수행하는 애가 Gunicorn이고, Django는 파이썬 앱이라고 할 수 있으며, 얘네가 함께 웹 어플리케이션 서버가 되는 것이다. Nginx는 여기서 Gunicorn+Django의 앞단에 위치하고 있는데, WSGI의 프로세스와는 별 관련 없이 buffering, reverse proxy나 load balance와 같은 별도의 일을 수행하게 되는 것이다.

## 2. WSGI의 동작 과정

WSGI에 대해 좀 더 감을 잡기 위해 [PEP333](https://www.python.org/dev/peps/pep-0333/#specification-overview)에 나와있는 WSGI의 동작 과정을 한 번 살펴보려고 한다. 다시 한 번 말하지만 WSGI는 별도의 프레임워크 같은 게 아니라, 동적인 데이터에 대응하기 위해서 웹 서버와 파이썬 웹 앱이 어떻게 서로 동작해야 하는지에 대한 내용을 담고 있는 specification이라고 할 수 있다.

공식 문서에서는 WSGI를 **"simple and universal interface between web servers and web applications or frameworks"**라고 설명하고 있으며, WSGI의 목적은 **"to facilitate easy interconnection of existing servers and applications or frameworks, not to create a new web framework"**라고 서술하고 있다.

WSGI는 server/gateway side와 application/framework side를 가지는데, server side에서 들어온 요청이 application side의 callable object를 호출(invoke)하게 된다. 여기서 callable object란 곧 파이썬 스크립트에서 정의한 application을 의미하고, object라고는 했지만 callable한 어떤 형태든지 상관은 없다.

![img](https://media.vlpt.us/images/jimin_lee/post/d5fd03ea-666a-4a0b-8a03-d574cd7a34f0/KakaoTalk_20210425_212448657.jpg)

`참고` **WSGI Middleware**

- WSGI server/gateway side와 application/framework side를 둘 다 구현하고 있는 하나의 프로그램
- 서버에 대해서는 어플리케이션의 역할을 수행하고, 어플리케이션에 대해서는 서버의 역할을 수행.
- 동작 과정 : 클라이언트 요청 → server side에서 middleware component를 호출 → middleware component가 application side의 application을 호출
- **Gunicorn, uWSGI**