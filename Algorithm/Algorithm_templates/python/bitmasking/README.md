# 비트마스킹

- 비트 연산을 이용한 테크닉
- 상태 저장, 방문 체크 등 true와 false로 상태를 나타낼 수 있는 상황에서 활용 가능
  - 0은 false, 1은 true를 나타냄



## 예시 1) 부분집합 구하기

- {1, 2, 3, 4} 의 부분집합을 구하는 경우

- {}, {1}, {2}, {3}, {4}, {1, 2}, {1, 3} ... 등 수를 출력해야 함

  - 0000 ~ 1111 이내로 집합에서 각 자리의 인덱스에 해당하는 비트 상태를 체크하면 된다
  - 예를 들어, i가 0101 일때 1를 2와 0만큼 << 연산을 하면, 각 자리에서 i와 & 연산했을 때 true가 된다. 

- ```python
  # 숫자 집합
  numbers = [1, 2, 3, 4]
  
  
  for i in range(1 << len(numbers)):
      for j in range(len(numbers)):
          # 1을 << 연산을 하여 i의 각 자리에 있는 수와 & 연산
          # j만큼 왼쪽으로 1을 밀었을 때 i의 해당 자리 비트가 1이라면 숫자 집합에서 그 자리에 해당하는 인덱스를 출력
          if i & (1 << j):
              print(numbers[j], end = ' ')
      print()
      
  ```



## 예시 2) 상태 체크하기

- 5 곳을 방문하는 상황을 가정

- 00000 ~ 11111 까지 0과 1로 상태를 체크할 수 있음

  - 0은 방문하지 않음, 1은 방문했음을 의미

- 첫번째부터 다섯번째 장소 중 두 번째 또는 세번째 장소를 방문하는 모든 경우를 찾을 때

  - 두번째 자리나 세번째 자리가 1로 체크되어 있으면 된다.

  - 코드 상으로 표현할 때는 오른쪽에서 왼쪽 순으로 순번을 매긴다.

    - 두번째 자리의 1를 체크하고 싶다면 00010, 세번째 자리의 1를 체크하고 싶다면 00100을 체크하는 방식
    - 이때 << 연산으로 각 자리의 비트를 체크하려면 해당 자릿수의 -1만큼 << 연산을 해야 한다.
      - 두번째 자리면 1을 1번만 << 연산을 해야 10으로 만들 수 있음
      - 물론 비트 자리를 000000 으로 전체 자릿수의 + 1 만큼 확보한다면 n을 1부터 시작하여 각 상태를 체크할 수 있음
        - 이때는 두 번째 마을을 체크하고 싶을 때 그냥 1 << 2으로 & 연산을 하면 된다.

  - ```python
    
    for i in range(1 << 5):
        if i & 1 << 1 or i & 1 << 2:
            print(format(i, 'b'))
    
    ```

- 주어진 상태에서 두번째나 세번째 장소를 방문했는지 여부를 체크하는 경우

  - `11101` 은 첫번째, 세번째, 네번째, 다섯번째 마을을 방문했음을 나타냄

  - << 연산으로 나타내면, (1 << 0 + 1 << 2 + 1 << 3 + 1 << 4)

  - 마찬가지로 두 번째나 세 번째가 1로 체크되어있는지를 체크하면 된다. 예시에서는 세 번째 마을을 방문했으므로 true

  - ```python
    
    status = (1 << 0) + (1 << 2) + (1 << 3) + (1 << 4)
    print('status: ', format(status, 'b'))
    if status & 1 << 1 or status & 1 << 2:
        print('true')
    else:
        print('false')
    
    ```

- 특정 장소에 다다랐을 때 방문체크하는 경우

  - | 연산자를 이용

  - 원래 상태에서 네번째 장소를 방문했을 때를 체크해야 한다면

    ```python
    origin = 0b00100 # 세번째 마을만 방문한 경우를 나타냄, 0b는 python 이진수 표현하는 방식
    print(format(origin | 1 << 3, 'b')) # output: 1100 
    ```





## 응용 문제) 백준 1194_달이 차오른다 가자

- [링크](https://www.acmicpc.net/problem/1194)

- BFS + 비트마스킹

- **현재 보유한 열쇠 상테에서 새로 획득한 열쇠를 추가할 때**와 **어떤 문을 현재 열쇠 상태로 열 수 있는지 여부를 체크할 때**  비트마스킹 활용 가능

```python
import sys
from collections import deque

input = sys.stdin.readline


N, M = map(int, input().split())
Map = [input().strip() for _ in range(N)]

checked = [[[False] * (2 ** 6 + 1) for _ in range(M)] for _ in range(N)]               # 현재 아무런 열쇠를 지니고 있지 않은 상태 표시 [r][c][열쇠 상태 체크]

# 비트마스킹
# value 값만큼 비트를 << 연산자로 이동
key_table = {
    'a' : 0, 'b' : 1, 'c' : 2, 'd' : 3, 'e' : 4, 'f' : 5
}

# 시작점 찾기
start = tuple()
for r in range(N):
    for c in range(M):
        if Map[r][c] == '0':
            start = (r, c)
            checked[r][c][0] = True
            break
    if start:
        break

# 0은 현재 아무런 열쇠도 가지고 있지 않은 상태
q = deque([[start, 0, 0]])                   # [출발점, 열쇠 상태, 거리]
dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

while q:
    s = q.popleft()

    r, c = s[0]
    key = s[1]
    dist = s[2]

    if Map[r][c] == '1':
        print(dist)
        exit()

    for d in dirs:
        nr = r + d[0]
        nc = c + d[1]
        # 방문이 가능한 경우
        if 0 <= nr < N and 0 <= nc < M and Map[nr][nc] != '#'  and not checked[nr][nc][key]:

            # 다음 칸이 열쇠 칸일 때, 내가 가지고 있지 않는 거라면 열쇠 상태 갱신 후 진입
            if 'a' <= Map[nr][nc] <= 'z':
                temp_key = key | (1 << key_table[Map[nr][nc]])
                checked[nr][nc][temp_key] = True
                q.append([(nr, nc), temp_key, dist + 1])

            # 다음 칸이 문 칸일 때, 내가 맞는 키를 가지고 있는 상태라면 진입
            elif 'A' <= Map[nr][nc] <= 'Z':
                if key & (1 << key_table[Map[nr][nc].lower()]):
                    checked[nr][nc][key] = True
                    q.append([(nr, nc), key, dist + 1])

            else:
                checked[nr][nc][key] = True
                q.append([(nr, nc), key, dist + 1])        
            
            
print(-1)
```

