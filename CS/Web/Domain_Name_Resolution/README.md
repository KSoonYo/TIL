## Domain Name Resolution

- 브라우저와 서버 간 통신을 하기 전에 도메인 네임을 IP 주소로 변환해주는 작업

-  www.google.com 처럼 IP 주소가 아닌 호스트의 도메인 이름으로 브라우저에 입력해도 구글 서버의 IP 조소로 변환되어 요청을 하게되는 데, 이때 도메인 네임을 IP 주소로 변환하는 작업이 **Domain Name Resolution**



![4: Domain name resolution process.](README.assets/Domain-name-resolution-process.ppm)

by Yakup Koc

**과정**

1. www.cnn.com 이라는 도메인으로 주소를 요청했다고 가정
   - DNS(Domain Name System)에 참여하는 서버를 **Name server(NS)** 라고 한다.
2. Recursive Resolver에 www.cnn.com 도메인에 해당하는 IP 주소가 있는지 요청, 있다면 바로 IP 주소를 응답
   - Recursive Resolver(Public Recursive Resolver 또는 Public DNS resolver):  요청한 도메인 주소에 대해서 IP 주소를 클라이언트에 응답하거나  authoritative DNS server에 요청을 분배하여 IP 주소를 알아내는 역할을 수행
   - Recursive Resolver 는 ISP나 외부 공급자에 의해 설정됨

3. IP 주소가 없다면 Resolver는 Root NS에 www.cnn.com에 해당하는 IP 주소를 요청, 없으면 .com으로 끝나는  도메인 네임을 관리하는 Name server(TLD server: Top Level Domain server)의 IP 주소를 응답

   - Root NS: 도메인 네임 시스템(DNS)의 Root zone. 

     - Root Domain: 계층적 구조의 시스템인 DNS의 최상단 계층. 인터넷 상의 모든 도메인 주소는 함축적으로 끝에 '.'으로 끝나며, 이 '.'에 해당하는 것이 Root domain이다.

     - ```
       www.example.com. 
       ```

     - Root Domain은 모든 최상위 도메인을 포함한다.

   - TLD: 최상위 도메인. 도메인 네임의 가장 마지막 부분을 뜻한다.(Root Domain '.'은 함축적인 것이므로 제외) 

4. Resolver는 TLD NS에 www.cnn.com에 해당하는 IP 주소를 요청, 없으면 cnn.com으로 끝나는 도메인 네임을 관리하는 Name Server(SLD server: Second Level Domain server)의 IP 주소를 응답

   - SLD: 2단계 도메인. 최상위 도메인 아래에 직접 위치한 도메인

5. Resolver는 SLD NS에 www.cnn.com에 해당하는 IP 주소를 요청, SLD 서버는 cnn.com에 해당하는 IP 주소를 반환

   - www는 sub domain이며 www를 포함하지 않은 cnn.com는 apex domain(어떠한 서브 도메인도 포함하지 않은 도메인)
     - sub domain은 말 그대로 주 도메인의 보조 도메인이며, 주로 웹사이트의 일부를 나타냄 
   - cnn.com으로 브라우저에 입력해도 www.cnn.com으로 redirect 되므로 www.cnn.com의 IP 주소와 cnn.com의 IP 주소는 동일
     - www는 주로 웹사이트의 홈페이지나 중요한 웹페이지를 나타낼 때 사용하는 서브 도메인

6. IP 주소를 얻었다면 클라이언트는 www.cnn.com 서버와 본격적으로 통신 시작
7. 이미 한번이라도 IP 주소를 받은 적이 있는 도메인 네임의 경우, OS가 해당 IP 주소를 계속 저장해두고 사용
   - 내 컴퓨터가 사용하는 가장 근처의 네임 서버 역시 자주 요청 받는 도메인 네임에 대해서 캐시로 관리하는 경우가 많음