# TCP/UDP
- 전송 계층(Transport layer) 프로토콜
- 프로세스 간 전달을 책임
  - 목적지 포트 번호를 확인하여 데이터 전달
- TCP
  - 패킷 사이의 순서를 보장
  - 가상회선을 사용하여 패킷 교환하는 가상회선 패킷 교환 방식 사용
  - 연결 지향 프로토콜 -> 패킷 수신 여부 확인
  - 흐름제어, 오류제어, 혼잡제어
- UDP
  - 패킷 순서를 보장하지 않음
  - 수신 여부 확인하지 않음
  - 단순히 데이터만 송수신하는 데이터그램 패킷 교환 방식 사용

