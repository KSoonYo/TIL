# OSI 7 layers

- Open Systems Interconnection(SOI)
- 1980년대 ISO에 의해 개발된 모델
- 네트워크 상에서의 통신 시스템과 프로오콜 디자인을 7가지 계층으로 나누어 설명
- 컴퓨터 네트워크 시스템 개념을 설명하는 가상의 개념적 모델
  - 목적
    - 각 계층마다 고유한 기능이 있으며, 프로토콜 또한 기능별로 구분
    - 각 계층은 하위 계층의 기능만을 사용하고, 상위 계층에게 기능을 제공
    - 네트워크 상에서 이루어지는 통신을 시각화하는 데 도움
      - 통신 과정에서 문제가 발생했을 때, 원인을 쉽게 파악할 수 있음

![What is OSI Model | Comprehensive Guide to OSI Model](README.assets/OSI-Model.png)

![OSI-Model1_Done](https://cdn.educba.com/academy/wp-content/uploads/2019/05/OSI-Model1_Done.jpg.webp)

## Layer 7 :Application Layer(응용 계층)

- 사용자(혹은 어플리케이션)가 네트워크 시스템에 접근할 수 있도록 기능 제공
- 다른 종단으로부터 들어오는 정보를 받아 데이터를 사용자에게 보여줌
- 일반적인 응용 서비스를 수행하는 계층
-  예시 서비스) 원격 로그인, 메일 서비스, HTTP 웹 통신, 파일 전송 및 엑세스, 웹 브라우저 등

### 대표 프로토콜

- FTP
- Telnet
- SMTP(Simple Mail Transfer Protocol)
- HTTP
- DHCP
- ...
- ...

## Layer 6: Presentation Layer(표현 계층)

- 응용 계층에서 전달된 데이터를 추출하여 필요한 포맷으로 처리한 후 네트워크로 전달
- 세션 계층에서 전달된 데이터를 사용자 시스템에 맞게 번역하여 전달
- 데이터의 형식상 차이를 다루는 부담을 응용 계층으로부터 덜어준다.
- 예시) ASCII to EBCDIC
- **기능**
  - Translation(번역)
  - Encryption/Decryption(암호화 및 복호화)
    - 평문을 암호화 혹은 암호화된 데이터를 평문으로 복호화
  - Comprssion(압축) : 네트워크 상에서 데이터가 전달 되는데 필요한 비트 수를 줄임



## Layer 5: Session Layer(세션 계층)

- 양 끝단의 응용 프로세스가 통신을 관리하기 위한 기능을 제공

- TCP/IP 세션 간 연결을 생성, 유지, 복구, 인증, 보안, 종료까지 모두 책임
  - 양 끝단이 통신을 하려면 세션이 필요
  - 이외에도 반이중 방식(half-duplex) , 전이중 방식 통신(Full-duplex), 체크포인팅, 다시시작, 통신 사용자 동기화 등 수행
- **기능**
  - Session establishment, maintenance, and termination : 두 프로세스 간 세션을 생성, 유지, 종료
  - Synchronization(동기화) : 데이터 내 동기화 지점(체크 포인트)를 추가
    - 동기화 지점을 통해 에러를 확인하여 적절하게 재동기화를 진행
    - 데이터 손실 회피
  - Dialog controller



### 대표 프로토콜

- RPC
- RTCP
- ZIP
- ...



## Layer 4: Transport Layer(전송 계층)

- 데이터를 전송하고 수신하는 기능
- 양 끝단의 사용자들이 신뢰성 있는 데이터를 주고 받을 수 있도록 기능 제공

- 시나리오
  - 송신 측
    - 상위 계층에서 포맷팅된 데이터를 받아 세그멘테이션
    - 세그멘테이션: 데이터 전송 과정에서 흐름, 오류 제어를 목적
    - 세그먼트 헤더 내에는 Source(발신지) 포트 넘버와 Destination(목적지) 포트 넘버가 추가되며, 세그먼트화된 데이터는 네트워크 레이어로 전달됨
  - 수신 측
    - 전송 계층에서 세그먼트 내 포트 넘버를 읽고 적절한 프로세스에 데이터 전달
    - 송신 측이 전송한 여러 세그먼트를 모아서 재조합하는 과정 수행
- 서비스
  - **OSI 7 계층의 전송 계층은 연결 지향이지만, TCP/IP 는 연결 지향과 비연결형 모두 고려**
  - Connection-Oriented Service(연결 지향서비스)
    - 전송 계층에서 다음 세 단계 과정이 이루어짐
      1. 연결 생성
      2. 데이터 전송
      3. 연결 종료
    - 송신 측은 데이터를 전달한 후, 수신 측에 데이터가 잘 전달되었는지 확인
    - 수신 측은 데이터를 전달받았으면 송신 측에 응답을 보냄
  - Connectionless Service(비연결형 서비스)
    - 데이터를 전송하기만 하고 전송이 완료되었는지 송신 측에서 확인을 하지 않음

### 대표 프로토콜

- TCP
- UDP



## Layer 3: Network Layer(네트워크 레이어)

- 네트워크 상에서 데이터를 목적지까지 전달하는 기능
- 데이터를 패킷으로 관리
- 네트워크 기기나 라우터에 의해 기능이 수행됨
- **기능**
  - Routing(라우팅) : 발신지에서 목적지까지 적절한 경로를 찾는 기능
  - Logical Addressing(논리적 주소) : 송신 측 IP 주소, 수신 측 IP 주소를 패킷 헤더에 추가
    - 네트워크 내 모든 호스트는 고유 주소를 찾추어야 함
  - 메시지 포워딩

### 대표 프로토콜

- IPv4, IPv6
- ICMP
- ARP
- ...



## Layer 2 :Data Link Layer(데이터 링크 계층)

- 점(노드) 대 점(노드) 간 신뢰성 있는 데이터 전송을 보장하기 위한 계층

- 네트워크 계층에서 전달된 패킷을 프레임 단위로 나누고, 수신 측의 물리적인 주소를 프레임 헤더에 추가
  - NIC(Network Interface Card)의 프레임 크기에 따라 패킷을 프레임으로 나눔
- NIC과 호스트 기기의 디바이스 드라이버에 의해 다루어짐
-  스위치와 브릿지는 대표적인 데이터 링크 계층 기기
- **기능**
  - Framing(프레임화) : 수신 측에 전달된 비트들의 집합(비트스트림)을 프레임화
    - 프레임의 시작과 끝에 특별한 비트 패턴을 추가
    - 추가된 비트는 흐름 제어, 접근 제어, 오류제어에 사용될 수 있음
  - Physical addressing(물리 주소화): 프레임 생성 이후, 송신 측의 물리 주소(MAC address)와 수신 측의 물리 주소를 프레임 헤더에 추가.
    - 물리 주소(MAC)는 NIC이 만들어질 때부터 정해짐
  - Error control(오류 제어) : 손실되거나 손상된 프레임에 대해 오유를 감지하여 재전송
  - Flow control(흐름 제어) : 수신자의 수신 데이터 전송률을 고려하여 데이터를 전송하도록 제어
  - Access control(접근 제어) : 주어진 어느 한 순간에 하나의 장치만 동작하도록 제어
    - 복수의 기기가 하나의 통신 채널을 공유하는 경우, 데이터 링크 계층은 어느 기기를 동작시킬지를 규정

- 예시
  - 이더넷
  - LLC
  - HDLC

### 대표 프로토콜

- ARP(IP to MAC)
- RARP(MAC to IP)
- ALOHA
- ...



## Layer 1 : Physical Layer(물리 계층)

- 물리적 매체를 통한 **비트스트림 전송**에 요구되는 기능을 담당(기계적, 전기적, 전송매체)
- 물리적인 장치와 인터페이스가 전송을 위해 필요한 기능과 처리절차 규정
- 네트워크의 기본 네트워크 하드웨어 전송 기술을 이루며, 다양한 특징의 하드웨어 기술이 접목되어 있음

- 데이터를 보낼 때에는 프레임을 0과 1의 데이터로 전환하여 다음 노드로 전송하고, 데이터를 받을 때에는 신호를 0과 1의 데이터로 전환하여 데이터 링크 계층으로 전송, 데이터 링크 계층은 0과 1의 데이터를 프레임화

- **기능**

  - Physical topologies : 서로 다른 장치(또는 노드)들이 네트워크 상에서 배치되는 방식을 특정

    - ex) bus, star, mesh topology
    - 장치와 전송매체 간의 인터페이스 특성을 규정

  - Bit synchronization(비트 동기화) : clock으로 비트 동기화 기능 수행, 송신자와 수신자는 같은 clock을 사용

  - Bit rate control(비트 전송률 제어) : 신호가 유지되는 비트의 주기를 규정(ex_초당 비트 수, bps)

  - Transmission node: 두 연결된 장치 간 데이터 흐름 방식을 규정

    - ex) Simplex, half-duplex, full-duplex

    

![Lightbox](README.assets/computer-network-osi-model-layers.png)





## TCP/IP 계층 모델과 차이점

- TCP/IP는 인터넷에서 컴퓨터들이 서로 정보를 주고 받는 데 쓰이는 통신 규약(By wikipedia)

- 일반적으로 인터넷 네트워크 통신은 TCP/IP 모델을 바탕으로 이루어짐
  - 네트워크 통신의 개념적인 설명은 OSI 7 계층을, 실제 인터넷 통신은 TCP/IP 모델을 바탕으로 이루어지는 경우가 많음
  - TCP/IP 모델은 네트워크 계층 중 인터넷 계층만 사용
  - OSI 7 계층은 인터넷 출현 이후, TCP/IP는 인터넷 출현 이전에 등장

- OSI 7 계층은 7개 layers, TCP/IP는 4개 layers
  - OSI 7 계층: Application, Presentation, Session, Transport, Network, Data link, Physical
  - TCP/IP : Application, Transport(TCP, UDP), Network(Internet, IPv4 / IPv6), Network Access(Link or Physical)

- OSI 7 계층은 인터페이스, 서비스, 프로토콜 간 구분이 명확하지만, TCP/IP는 그렇지 않음
- OSI 7 계층 헤더의 최소 크기는 5bytes, TCP/IP는 20bytes
- OSI 7 계층은 서로 다른 시스템 간 네트워크 통신에 대한 개념적 모델이며 인터페이스의 복잡도를 낮추고 표준화 하는 데 유용
- TCP/IP 모델은 특정 컴퓨터가 인터넷에 연결되어 다른 컴퓨터와 통신하는 방법을 파악하는 데 유용

# References

- 패스트캠퍼스 컴퓨터 네트워크 강의

- https://www.imperva.com/learn/application-security/osi-model/

- https://www.geeksforgeeks.org/layers-of-osi-model/

- https://www.networkworld.com/article/3239677/the-osi-model-explained-and-how-to-easily-remember-its-7-layers.html

