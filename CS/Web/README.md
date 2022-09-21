# Web

[WEB(TCP School)](http://www.tcpschool.com/webbasic/www)

- World Wide Web의 약자
  - WWW나 W3이라고도 부른다.

- 웹브라우저를 통해 이동할 수 있는 가상의 연결망

- 인터넷에서 가장 많은 비중을 차지하는 서비스가 웹
- 인터넷 상에서 텍스트나 그림, 소리, 영상 등과 같은 멀티미디어 정보를 `하이퍼텍스트` 방식으로 연결하여 제공



## URL

- Uniform Resource Locator

- 인터넷에서 웹 페이지, 이미지, 비디오 등 리소스의 위치를 가리키는 문자열
- 웹에서 접근 가능한 다양한 종류의 데이터들을 URL로 식별



### URL 구조

[URL 구조 예시(MDN 문서)](https://developer.mozilla.org/ko/docs/Learn/Common_questions/What_is_a_URL)

> URL 예시)
>
> https://www.serviceDomain.com/path/detail?title=a&info=something

- `https://`
  - scheme(스킴) : 프로토콜의 이름
- `www.serviceDomain.com`
  - host(호스트): 웹 도메인
- `/path/detail`
  - path(경로): 서버에 있는 데이터 중 원하는 데이터를 특정
  - 예시는 path/detail 경로에 있는 데이터를 요청하는 것을 의미
- `?title=a&info=something`
  - query(쿼리) : 데이터에 관한 세부적인 요구사항
  - 예시는 path/detail에 있는 데이터에서 title이 a이고 info가 something인 데이터를 특정하여 요청하는 것을 의미



## When a URL is entered into a browser...

1. 웹브라우저는 URL에서 호스트를 보고 **도메인 네임 리졸루션(Domain Name Resolution)** 작업을 수행하여 요청을 보낼 서버 식별
2. 해당 서버로 request 요청.(URL에서 path 이후의 부분들을 request에 담아서 전송)
3. 요청을 받은 서버는 request의 path 이후의 부분들을 보고, 그것이 의미하는 데이터를 찾아 결과를 response에 담아서 응답
4. response를 받은 브라우저는 response의 내용을 사용자에게 보여줌

