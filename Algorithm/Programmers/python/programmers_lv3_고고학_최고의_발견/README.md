# 문제
https://school.programmers.co.kr/learn/courses/30/lessons/131702

# 풀이
- **핵심 1)** 각 퍼즐 조각의 회전은 아래 행이 윗 행에 종속되어 있다.
  - 만약 현재 퍼즐 조각의 바로 위에 있는 조각이 0이라면 현재 조각은 돌릴 필요가 없다.
  - 위에 있는 퍼즐 조각이 0을 가리키도록 회전을 해야 한다.
- **핵심 2)** 맨 윗 줄에 있는 퍼즐 조각은 종속되는 행이 없으므로 맨 윗 줄에 있는 각각의 퍼즐 조각이 몇 번 회전 했는지에 대하여 모든 경우를 고려해야 한다.

```python
from itertools import product


def solution(clockHands):
    global answer
    answer = float('inf')
    def rotate(N, pieces, turns, i, cnt):
        global answer
        
        if cnt > answer:
            return
        
        # i행에 있는 모든 퍼즐 조각 회전
        for j in range(N):                            
            for ndir in [[0, 0], [-1, 0], [1, 0], [0, -1], [0, 1]]:
                ni, nj = i + ndir[0], j + ndir[1]
                if 0 <= ni < N and 0 <= nj < N:
                    pieces[ni][nj] = (pieces[ni][nj] + turns[j]) % 4
        
        if i == N - 1:                                                # 마지막 행의 모든 퍼즐 조각이 회전했다면 최소값 갱신
            temp = 0
            for row in pieces:                                        # 보드의 모든 퍼즐 조각이 0을 가리키는지 체크
                temp += sum(row)
            if not temp:
                answer = min(cnt, answer)
            return
        
        next_turns = [(4 - pieces[i][k]) % 4 for k in range(N)]       # 다음 행의 퍼즐조각이 현재 행의 퍼즐조각이 0이 되도록 돌려야 하는 회전 수
        rotate(N, pieces, next_turns, i + 1, cnt + sum(next_turns))
        return
    
    N = len(clockHands)
    start = 0
    for turns in product([i for i in range(4)], repeat = N)****:
        pieces = []
        for row in clockHands:
            pieces.append(row[:])
        rotate(N, pieces, turns, 0, start + sum(turns))
    return answer
```