# Socket

**네트워크 계층 모델**

![OSI 7](https://user-images.githubusercontent.com/24274424/86514723-94b77900-be4e-11ea-8456-ad39b27d9ba9.png)

https://snyung.com/content/2020-08-31--%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-%EA%B8%B0%EC%B4%88-osi-7-%EA%B3%84%EC%B8%B5%EA%B3%BC-tcp-ip-%EA%B3%84%EC%B8%B5/





```
Sockets on the other hand are an API that most operating systems provide to be able to talk with the network. The socket API supports different protocols from the transport layer and down.
```

- HTTP 는 Application layer protocol 
- TCP/UDP는 Transport layer protocol
- 기본적으로 네트워크 통신은 end-to-end 통신

```

client - 7 - 6 - 5 - 4 - 3 - 2 - 1 -> request -> server

			1 - 2 - 3 - 4 - 5 - 6 - 7 <- response

```

- 따라서 서로 다른 통신 규약(프로토콜)을 사용하는 transport layer와 application layer 사이에서 프로토콜을 적절하게 decode/encode 해주는 인터페이스 역할이 필요.

  => 그 역할을 `socket`이 담당

- client 측에서 server로 요청을 보낼 때

  1. http 프로토콜로 요청을 보내는데, socket이 해당 프로토콜에 적힌 내용들을 TCP 프로토콜(또는 UDP) 규약에 맞게 포장 

  2. request를 받은 server측, TCP 프로토콜을 HTTP 프로토콜로 포장 해제, 이제 HTTP 프로토콜로 보내는 응답을 TCP 프로토콜로 포장
  3. response를 받은 client, 앞서 서버와 동일한 방법으로 포장 해제, 서버측에게 잘 받았다고 응답 보내고 connection 종료!

=> 이 때 포장과 포장해제를 해주는 역할을 socket이 맡는다.(socket )

그래서 기본적으로 매번 요청과 응답을 보내고 받을 때 반드시 socket을 구현해줘야 하지만, 개발자들이 잘 구현해놓은 것들이 있으니 가져다 쓰면 된다.



**HTTP Connection**

- HTTP connection is a protocol that runs on a socket.
- HTTP connection is a higher-level abstraction of a network connection.
- With HTTP connection the implementation takes care of all these higher-level details and simply send HTTP request (some header information) and receive HTTP response from the server.

**Socket Connection**

- Socket is used to transport data between systems. It simply connects two systems together, an IP address is the address of the machine over an IP based network.
- With socket connection you can design your own protocol for network connection between two systems.
- With Socket connection you need to take care of all the lower-level details of a TCP/IP connection.

**참조**

https://stackoverflow.com/questions/15108139/difference-between-socket-programming-and-http-programming