# Nginx

**Nginx**(엔진 x라 읽는다)는 [웹 서버 소프트웨어](https://ko.wikipedia.org/wiki/웹_서버_소프트웨어)로, 가벼움과 높은 성능을 목표로 한다. [웹 서버](https://ko.wikipedia.org/wiki/웹_서버), [리버스 프록시](https://ko.wikipedia.org/wiki/리버스_프록시) 및 메일 프록시 기능을 가진다.

2017년 10월 기준으로 실질적으로 작동하는 웹 사이트(active site)들에서 쓰이는 [웹 서버 소프트웨어](https://ko.wikipedia.org/wiki/웹_서버_소프트웨어) 순위는 [아파치](https://ko.wikipedia.org/wiki/아파치)(44.89%), 엔진엑스(20.65%), [구글 웹 서버](https://ko.wikipedia.org/wiki/구글_웹_서버)(7.86%), 마이크로소프트 [IIS](https://ko.wikipedia.org/wiki/IIS)(7.32%)순이다.[[1\]](https://ko.wikipedia.org/wiki/Nginx#cite_note-1) 이 조사에서 생성은 되어있으나 정상적으로 작동하지 않는 웹 사이트들은 배제되었으며[[2\]](https://ko.wikipedia.org/wiki/Nginx#cite_note-2) 특히 MS의 [인터넷 정보 서비스](https://ko.wikipedia.org/wiki/인터넷_정보_서비스)([IIS](https://ko.wikipedia.org/wiki/IIS))를 설치한 웹 사이트들의 상당수가 비활성 사이트였다. 그런 사이트들도 포함하면 MS IIS가 1위이다. 2017년 6월 현재 Nginx는 한국 전체 등록 도메인 중 24.73%가 사용하고 있다.[[3\]](https://ko.wikipedia.org/wiki/Nginx#cite_note-3)

Nginx는 요청에 응답하기 위해 비동기 [이벤트 기반](https://ko.wikipedia.org/wiki/이벤트_(컴퓨팅)) 구조를 가진다. 이것은 [아파치 HTTP 서버](https://ko.wikipedia.org/wiki/아파치_HTTP_서버)의 스레드/프로세스 기반 구조를 가지는 것과는 대조적이다. 이러한 구조는 서버에 많은 부하가 생길 경우의 성능을 예측하기 쉽게 해준다.

https://ko.wikipedia.org/wiki/Nginx



- 역할

  - 정적 파일을 처리하는 HTTP 서버로서의 역할

    - HTML, CSS Javascript, 이미지와 같은 정보를 웹 브라우저(Chrome 등)에 전송하는 역할을 한다.(Http 프로토콜 준수)

      ![nginx_process](http://i.imgur.com/Zpw9D7x.png)

  - 응용프로그램 서버에 요청을 보내는 리버스 프록시(reverse proxy)로서의 역할

    - 클라이언트가 가짜 서버(proxy)에 요청을 하면, 서버가 배후 서버(reverse server)로부터 데이터를 가져오는 역할. 프록시 서버가 `Nginx`, 리버스 서버가 `응용프로그램 서버`
    - 웹 응용프로그램 서버에 리버스 프록시(Nginx)를 두는 이유는 요청(request)에 대한 버퍼링이 있기 때문이다. 클라이언트가 직접 App 서버에 직접 요청하는 경우, 프로세스 1개가 응답 대기 상태가 되어야만 한다. 따라서 프록시 서버를 둠으로써 요청을 `배분`하는 역할을 한다.
    - Nginx.conf 파일에서 `location` 지시어를 사용하여 요청을 배분한다.

    ![비동기 처리방식](http://i.imgur.com/W6JATVH.png)

    - Nginx는 비동기 처리(Event-Drive) 방식 채택

    참고: https://whatisthenext.tistory.com/123

    

    +)

    - 포워드 프록시는, 내부망에 함께 있는 클라이언트가 인터넷을 통해 어딘가에 있는 서버로 요청을 보내려고하면 이 요청을 받아 연결해준다. **클라이언트** 앞단에서의 처리!

    - `리버스 프록시`는, 내부망의 **서버** 앞단에서 요청을 처리한다.

      내부 서비스가 직접 서비스를 제공해도 되지만.. 이렇게 구성하는 이유는 보안때문이다. WAS(웹어플리케이션서버)는 대부분 DB 서버와 연결 되어있으므로, WAS 가 최전방에 있으면 보안에 취약해진다. 그때문에 리버스 프록시를 두고 사용한다면 WS 가 WAS 와 통신해서 결과를 클라이언트에 제공하는 방식으로 서비스를 하게 된다.

      https://juneyr.dev/nginx-basics

    

## webserver

웹서버는 다른 말로 HTTP Server라고도 부른다. 웹브라우저의 카운터 파트너로서 서버 쪽에서 정보를 제공하는 소프트웨어를 의미한다. 대표적인 웹서버는 [Apache](http://httpd.apache.org/)가 있다. 아래 그림은 웹서버의 시장 점유율을 보여준다. (참고 [netcraft.com](http://news.netcraft.com/archives/2013/01/07/january-2013-web-server-survey-2.html))

![img](https://s3.ap-northeast-2.amazonaws.com/opentutorials-user-file/module/384/1394.gif)

- NGINX는 차세대 웹서버로 불린다. 위의 그래프를 통해서 알 수 있듯이 Apache의 독주에 제동을 걸고 있다. NGINX의 특징은 한마디로 정의하면 아래와 같다.

  > 더 적은 자원으로 더 빠르게 데이터를 서비스 할 수 있다.



## Nginx 디렉토리 구조

> 설치 방식, 운영체제에 따라 조금씩 상이할 수 있다.



![nginx conf](https://juneyr.dev/static/6d1b2a8738f31f650b58cea9b7d8f10f/7d769/1.png)

https://juneyr.dev/nginx-basics



(윈도우 설치)

```
├─conf // 위의 conf 파일 트리와 동일
├─contrib
│  ├─unicode2nginx
│  └─vim
│      ├─ftdetect
│      ├─ftplugin
│      ├─indent
│      └─syntax
├─docs
├─html
├─logs
└─temp
```



### nginx.conf(nginx 설정)

## 설정 파일의 역할

- nginx.conf : 메인 설정 파일. 
- fcgi.conf : FastCGI 환경설정 파일
- sites-enabled : 활성화된 사이트들의 설정 파일들이 위치. 아파치에서는 Virtual host의 설정에 해당한다. 기본적으로 존재하지 않을수도 있다.
- sites-available : 비활성화된 사이트들의 설정 파일들이 위치

https://opentutorials.org/module/384/4526



```bash
worker_processes  1;
2events {
3    worker_connections  1024;
4}
5http { 
6    include       mime.types;
7    server {
8        listen       80;
9        location / {
10            root   html;
11            index  index.html index.htm;
12        }
13    }
14}
```



- `worker_processes` : 몇개의 워커 프로세스를 생성할 것인지 지정하는 지시어. 1이면 모든 요청을 하나의 프로세스로 실행하겠다는 뜻. CPU 멀티코어 시스템에서 1이면 하나의 코어만으로 요청을 처리하는 셈이다. auto로 놓는 경우가 많다.
  - 이와 같은 설정을 **core 모듈** 설정이라고 한다. nginx 설정값을 정하는 경우가 대부분 이에 해당한다.
- `events` 블록 : 이벤트 블록은 네트워크 동작방법과 관련된 설정이다.
  - `worker_connections` : 하나의 프로세스가 처리할 수 있는 커넥션의 수
  - 고로 최대 접속자수는 worker_processes X worker_connections가 된다. 🙂
- `http` 블록 : 하위에 server 블록, 그리고 location 블록을 갖는 **루트 블록** 이다. 여기서 선언된 값은 하위 블록에 상속된다. 서버의 기본값이 된다.
  - `include` : server 블록에서도 사용할 수 있다. `conf.d` 에 정의해놓은 파일들을 적용하는데 사용된다.
- `upstream` 블록: origin 서버라고도 한다. 여기서는 WAS 를 의미하고, nginx는 downstream에 해당한다고 할 수 있다. 여러 서버를 지정해두고, weight 을 정할 수 있다.



![upstream](https://juneyr.dev/static/49c50337e630f908d64c230bbe8e20d9/7d769/upstream.png)

위의 그림처럼, upstream은 여러개를 만들 수 있다. 어떤 요청은 A로, 또다른 요청은 B로 보내고자 할 때 쓰인다. 대표적인으로 api 서버를 지정하고, FE에서 특정 location 요청을 proxy 할 때 쓰인다.



```bash
upstream backend {
	server backend.juneyr.dev:443;3    
	keepalive 100;  }

server {
	listen       80;
    server_name  fe.juneyr.dev;
    
	location /v1 {
		proxy_pass https://backend;  
	}
```

- - `server` : 값으로 `host주소:포트` 가 온다.
  - `keepalive`: keepalive 로 유지시키는 최대 커넥션 수. keepalive로 유지하면 매번 TCP handshake를 하지 않아도 된다.
  - 자세한 값은 [공식 홈페이지](http://nginx.org/en/docs/http/ngx_http_upstream_module.html) 를 참고한다.

- `server` 블록: 하나의 웹사이트를 선언하는데 사용된다. server 블록이 여러개이면, 한대의 머신(호스트)에 여러 웹사이트를 서빙할 수 있다.
  - 이런 개념을 **가상 호스트**라고 한다. 실제로 호스트는 한대지만, 가상으로 마치 호스트가 여러개 존재하는 것처럼 동작하게 할 수 있다.



![virtualhost](https://juneyr.dev/static/41297646b45d36a4eec7e40fc898866f/7d769/virtualhost.png)



​	위 그림에서는 유저가 juneyr.dev, 그리고 augustyr.dev 로 각각 접속하는 경우를 나타낸다. 각각의 사이트는 같은 IP 머신(=호스트, 컴퓨터, 서버)로 연결되지만, 다른 페이지를 보여주도록 설정할 수 있다. 마치 정말 **다른 host**를 바라보는 것처럼!

​		listen : 이 웹사이트가 바라보는 포트를 의미한다.

​		server_name: 클라이언트가 접속하는 서버 (주로 도메인). 이것과 실제 들어온 request의 header에 명시된 값이 일치하는지 확인해서 분기한다.

​		root : 웹사이트가 바라보는 root 폴더의 경로를 의미한다.



- `location` 블록: server 블록안에 등장해서, 특정 웹사이트의 url 을 처리하는 데 사용한다. 예를 들어 `https://juneyr.dev/internal` 과 `https://juneyr.dev/apple-app-site-association` 로 접근하는 요청을 다르게 처리하고 싶을 때 사용할 수 있다.
- proxy_pass : 위에 설정한 upstream으로 넘길 수 있다.
- return : http status 코드를 임의로 넘길 수 있다.

```bash
location / {
	root /home/deploy/juneyr-dev;3    
	index index.html;  
	}
location /internal {
	return 200; 
	}
	
location /apple-app-site-association {
	default_type application/json 
	} # 이 경로에 실제로 해당 파일이 있음
```



출처: https://juneyr.dev/nginx-basics



+) 참고하면 좋은 블로그

https://madfishdev.tistory.com/3?category=855361

(Nginx 설치, hosting 설정 방법, uWSGI 연동 방법 상세히 설명)



---



# uWSGI



**uWSGI**는 [호스팅 서비스](https://ko.wikipedia.org/wiki/호스팅_서비스) 빌드를 위한 풀 스택 개발에 초점을 둔 [응용 소프트웨어](https://ko.wikipedia.org/wiki/응용_소프트웨어)이다.[[3\]](https://ko.wikipedia.org/wiki/UWSGI#cite_note-uwsgi-3) 프로젝트가 지원하는 최초의 플러그인이었던 [WSGI](https://ko.wikipedia.org/wiki/WSGI)(웹 서버 게이트웨이 인터페이스)의 이름을 따서 만들어졌다.[[3\]](https://ko.wikipedia.org/wiki/UWSGI#cite_note-uwsgi-3)

uWSGI는 uWSGI의 네이티브 uwsgi 프로토콜의 직접 지원을 제공하는 [Cherokee](https://ko.wikipedia.org/w/index.php?title=Cherokee&action=edit&redlink=1), [Nginx](https://ko.wikipedia.org/wiki/Nginx) 등의 [웹 서버](https://ko.wikipedia.org/wiki/웹_서버)와 결합하여 [파이썬](https://ko.wikipedia.org/wiki/파이썬) [웹 애플리케이션](https://ko.wikipedia.org/wiki/웹_애플리케이션)을 서비스하기 위해 종종 사용된다.[[4\]](https://ko.wikipedia.org/wiki/UWSGI#cite_note-digitalocean-4)

참고: https://ko.wikipedia.org/wiki/UWSGI



python으로 웹 개발을 하려고하면 WSGI라는 걸 마주치기 마련이다. uWSGI란 WSGI라는 규칙을 따라서 만들어진 소프트웨어이며 **정적인 웹 서버(Apache / Nginx)와 python으로 작성된 Web Framework(Flask / Django) 사이의 통신을 도와주는 역할**을한다.

그렇다면 WSGI라는 규칙은 무엇일까? 기본적으로 웹 서버는 HTTP 형식의 요청을 받아서 처리한 뒤 응답해주는 기능을 한다. 이와 같은 처리은 1차적으로 nginx를 통해 이루어지며 서버에서 처리해야 할 작업이 있다면 Django와 같은 WAS(Web Application Server)가 필요하다. 하지만 Django는 python으로 이루어져있기 때문에 HTTP 요청을 이해할 수 없는데 이때에 uWSGI와 같은 소프트웨어가 필요한 것이다. **즉, 파이썬 어플리케이션이 웹 서버와 통신하기 위한 명세라고 보면 된다.**

uWSGI는 일종의 어플리케이션 컨테이너(Application Container)로써 동작한다고 볼 수 있다. 적재한 어플리케이션(Django)을 실행만 시켜주는 역할을 하기 때문이다.

최종적으로 Django가 돌아가는 환경을 그려보면 아래와 같을 것이다.

```
Client <-> Nginx <-> uWSGI <-> Django
```



출처: https://jinmay.github.io/2019/05/01/django/django-uwsgi-2/



요약

- WSGI는 Client의 request를 받아서 Django앱을 실행하고 서비스를 제공할 수 있게 도와주는 일을 하며 python 만의 표준
- 그러나 웹서버는 WSGI를 이해하지 못한다. 따라서 웹서버와 django 앱 사이에서 WSGI 표준을 웹서버가 이해할 수 있도록 연결해주는 징검다리가 필요한데, 이 역할을 uWSGI가 한다.
- uWSGI는 WSGI 구현체이다.

참고: https://velog.io/@tn841/Django-with-uWSGI-nginx



## 1. 왜 django의 runserver로 배포 하면 안돼요?

django에서는 runserver를 통해 개발 및 테스트를 합니다. 네. runserver는  “**개발 및 테스트**”가 목적입니다. 

django의 공식 문서에의 runserver의 글입니다. 

(https://docs.djangoproject.com/en/2.2/ref/django-admin/#runserver)

DO NOT USE THIS SERVER IN A PRODUCTION SETTING. It has not gone through security audits or performance tests. (And that’s how it’s gonna stay. We’re in the business of making Web frameworks, not Web servers, so improving this server to be able to handle a production environment is outside the scope of Django.)

"프로덕션 세팅으로 서버를 사용하지 마세요. 보안과 성능 테스트를 거치지 않았습니다. …. 프로덕션 환경은 django의 영역을 벗어난 것입니다.”

네. 공식적으로 프로덕션으로 사용하지 말라고 되어 있습니다. runserver의 성능은 매우 느리며, 보안에 대한 문제가 내포되어 있습니다. (여기서의 보안은 통신상의 보안입니다.) 프로덕션일 경우엔 wsgi를 통해서 서비스하도록 권장합니다. 

 

## 2. wsgi를 써서 django를 실행했으면 끝 아닌가요? 왜 nginx를 앞에 붙이나요?

wsgi를 쓴다면 django 등의 웹 프레임워크 기능을 할 수 있게 됩니다. 하지만 여기에 nginx를 앞에 붙이면 더 좋은 성능을 낼 수 있습니다. 

예를 들어 몇몇 wsgi는 ssl과 정적 파일을  지원 하지 않습니다. ssl과 정적파일을  django까지 요청이 도착한 다음에 처리해야 하므로 성능이 저하됩니다. 또한 DOS 공격과 같은 많은 요청을 nignx에서 처리 및 분산시킴으로써 서버 기능을 보장할 수 있게 됩니다. 

( uwsgi는 ssl과 정적 파일 지원이 가능합니다. 하지만 다른 wsgi보다 메모리와 cpu를 더 많이 소비합니다. )

![img](https://1.bp.blogspot.com/-jn8HQJiyNFk/XV0UCBj6oDI/AAAAAAAAArk/Ku9jK_5EmygYNDoWXanOWWz17TLZy7pzwCLcBGAs/s640/django.png)

## nginx가 수행하는 일

- 도메인 라우팅을 관리합니다 (리버스 프록시).
- 정적 파일 제공
- 한 번에 들어오는 많은 요청을 처리
- 느린 클라이언트 처리
- 동적 요청을 wsgi에 전달
- SSL (https)
- Python 코드와 비교하여 컴퓨팅 리소스 (CPU 및 메모리) 절약
- 로드 밸런싱, 캐싱 등

## uwsgi가 수행하는 일

- 작업자 프로세스 / 스레드 풀 실행 (코드 실행)
- Nginx에서 들어오는 요청을 UWSGI와 호환되도록 번역
- 앱의 UWSGI 응답을 적절한 http 응답으로 변환
- 요청이 들어오면 실제로 파이썬 코드를 호출합니다.



출처: https://uiandwe.tistory.com/1268 [조아하는모든것]





## Nginx + uWSGI + Django



설치 및 설정: https://velog.io/@tn841/Django-with-uWSGI-nginx#concept

공식문서 튜토리얼 : https://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html

(Unix 계열 시스템 환경을 전제로 함)





# gunicorn



## [Gunicorn 란? 쓰는 이유는?](https://leffept.tistory.com/345#Gunicorn%--%EB%-E%--%-F%--%EC%--%B-%EB%-A%--%--%EC%-D%B-%EC%-C%A-%EB%-A%--%-F)

Gunicorn은 Python WSGI로 WEB Server(Nginx)로부터 서버사이드 요청을 받으면 WSGI를 통해 서버 애플리케이션(Django)로 전달해주는 역할을 수행한다. Django의 runserver 역시도 똑같은 역할을 수행하지만 보안적으로나 성능적으로 검증이 되지 않았기 때문에 production 환경에서는 사용할 수 없다.(개발용으로는 유용하다)

 

### [produciton 환경에 적합한 Gunicorn](https://leffept.tistory.com/345#produciton%--%ED%--%--%EA%B-%BD%EC%--%--%--%EC%A-%--%ED%--%A-%ED%--%-C%--Gunicorn)

WSGI는 멀티 쓰레드를 만들 수 있기 때문에 Requset 요청이 많아지더라도 효율적으로 처리할 수 있다. 즉, production 환경에 적합하다.



![img](https://blog.kakaocdn.net/dn/c8411Q/btq9e5z4ovy/w0FxZDTT0gXKxk3OtjRe4k/img.png)

참고: https://leffept.tistory.com/345#produciton%--%ED%--%--%EA%B-%BD%EC%--%--%--%EC%A-%--%ED%--%A-%ED%--%-C%--Gunicorn



## uWSGI와 차이

`gunicorn`은 간단하고 서버의 리소스를 적게 쓰며 빠르고, `uwsgi`는 pure C언어로 구현되었기 때문에 좀 더 하드한 서비스를 위해 디자인되었다고 한다.

참고: https://velog.io/@primadonna/uWSGI-gunicorn%EC%9D%98-%EC%B0%A8%EC%9D%B4



# Daphne

> django-chnnels 라이브러리 설치하면 자동으로 설치되기도 한다.



Daphne is a HTTP, HTTP2 and WebSocket protocol server for [ASGI](https://github.com/django/asgiref/blob/main/specs/asgi.rst) and [ASGI-HTTP](https://github.com/django/asgiref/blob/main/specs/www.rst), developed to power Django Channels.

It supports automatic negotiation of protocols; there's no need for URL prefixing to determine WebSocket endpoints versus HTTP endpoints.

https://github.com/django/daphne (daphne github)



**Daphne은 Django Channels를 지원하기 위해 개발된 HTTP, HTTP2, WS 프로토콜 서버**로서, HTTP와 WS 요청을 받아들여서 자동으로 어떤 프로토콜로 처리해야 할지 스스로 결정합니다.

https://victorydntmd.tistory.com/265





# Redis



참고: https://brunch.co.kr/@jehovah/20



REDIS는 다음 특징을 갖는 data structure 이다.

1. Remote 에 위치한
   2. 프로세스로 존재하는
      3. In-Memory : 메모리 기반의
         4. “키-값” 구조 데이터 관리 시스템 : 비 관계형이며, 키-값 구조이기 때문에 별도 쿼리 없이도 데이터를 간단히 가져올 수 있다.

레디스는 위 특징을 가지고 크게 5가지 `String`, `Set`, `Sorted Set`, `Hash`, `List` 자료구조를 지원하는데,
서비스의 특성이나 상황에 따라 이걸 **1) 캐시**로 사용할 수도 있고, **2) Persistence Data Storage** 로 사용할 수도 있다.



**주요 특징**

- Single Threaded

  - 처리 시간이 긴 명령어가 들어오면 그 뒤 명령어들은 전부 대기

- `collection` 제공

- `remote data storage` 로서 여러 서버에서 같은 데이터를 공유하고 싶을 때 많이 사용

  ex) 인증 토큰 저장 등

https://velog.io/@hyeondev/Redis-%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%BC%EA%B9%8C



+)

참고하면 좋은 블로그 글

https://jyejye9201.medium.com/%EB%A0%88%EB%94%94%EC%8A%A4-redis-%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80-2b7af75fa818

(비관계형데이터베이스 개념, Redis 개념, 특징을 상세하게 설명)



# Nginx+uWSGI+gunicorn+Daphne with django channels

> django-chennels  채팅앱 배포하기

Nginx <-> (웹소켓) Daphne <-> django

Nginx <-> (정적 파일) /static  uwsgi or gunicorn <-> django



![Image for post](https://miro.medium.com/max/820/1*9B448P2lHqg3zb_-oXaFHQ.png)

https://ritiktaneja.medium.com/configuring-asgi-django-application-using-daphne-and-nginx-server-59a90456fe17



- Daphne로 http 요청 처리도 가능하긴 하지만, 정적파일은 효과적으로 처리하지 못한다. 그래서 일반적으로 Nginx를 reverse proxy로 둬서 Http 요청을 gunicorn이나 uWSGI로 처리하고, 비동기적인 WS(웹소켓) 요청은 Daphne 가 처리하도록 구성한다.

참고: https://victorydntmd.tistory.com/265 (django chnnels 앱과 Nginx, Daphne, uWSGI 연동하는 법이 구체적으로 설명되어있다.)





