# 문제

https://school.programmers.co.kr/learn/courses/30/lessons/92344

# 풀이

참고: https://tech.kakao.com/2022/01/14/2022-kakao-recruitment-round-1/

---

## 1번째 풀이

- 완전탐색(BFS)로 풀이 -> 시간 초과

```python
# 효율성 테스트 fail
from collections import deque

def recovery(board, r1, c1, r2, c2, degree, destroyed):
    visited = set()
    q = deque([(r1, c1)])               # [(r, c)]
    visited.add((r1, c1))
    while q:
        pos_r, pos_c = q.popleft()
        board[pos_r][pos_c] += degree
        if board[pos_r][pos_c] > 0 and (pos_r, pos_c) in destroyed:
            destroyed.remove((pos_r, pos_c))
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for dr, dc in dirs:
            nr = pos_r + dr
            nc = pos_c + dc
            if r1 <= nr <= r2 and c1 <= nc <= c2 and (nr, nc) not in visited:
                visited.add((nr, nc))
                q.append((nr, nc))
    return

def destroy(board, r1, c1, r2, c2, degree, destroyed):
    visited = set()
    q = deque([(r1, c1)])               # [(r, c)]
    visited.add((r1, c1))
    while q:
        pos_r, pos_c = q.popleft()
        board[pos_r][pos_c] -= degree
        if board[pos_r][pos_c] <= 0 and (pos_r, pos_c) not in destroyed:
            destroyed.add((pos_r, pos_c))
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for dr, dc in dirs:
            nr = pos_r + dr
            nc = pos_c + dc
            if r1 <= nr <= r2 and c1 <= nc <= c2 and (nr, nc) not in visited:
                visited.add((nr, nc))
                q.append((nr, nc))
    return

def solution(board, skill):
    N, M = len(board), len(board[0])
    destroyed = set()
    for typ, r1, c1, r2, c2, degree in skill:
        if typ == 1:
            destroy(board, r1, c1, r2, c2, degree, destroyed)
        else:
            recovery(board, r1, c1, r2, c2, degree, destroyed)
    answer = N * M - len(destroyed)
    return answer
```

---

## 2번째 풀이

- 누적합(prefix sum)을 이용한 풀이
- 원리)
  - 1차원 배열 `[1, 2, 5, 7]` 이 있을 때, 0번째 원소에서 2번째 원소까지 3을 더하고 싶다면?
    - 1번째 방법: for문을 돌면서 각각의 원소에 3을 더해준다. -> O(n) 시간 복잡도 소요
    - 2번째 방법: 누적합으로 구함
      - 0번째 원소에 3, 2번째 원소 다음 원소에 -3을 한 배열 선언
        - [3, 0, 0, -3]
        - 이를 누적합을 해주면 [3, 3, 3, 0] 으로 원하는 구간(0부터 2번째 원소) 내 변화량을 한 번에 더해줄 수 있음
        - 즉 시작 원소에 n, 마지막 원소의 다음 원소에 -n을 해주면 된다.(n은 변화량)
      - `원래 배열 원소[i] + 누적합 배열 원소[i]` 를 하면 각 원소에 변화량이 계산되므로 시간복잡도는 O(1)로 줄어든다.
- 2차원 배열로 누적합 아이디어 확장

  1. 각 행 별로 1차원 배열의 변화량을 누적합으로 구할 수 있는 배열을 구하고
  2. 각 열 별로 1차원 배열의 변화량을 누적합으로 구할 수 있는 배열을 구한다.

  - 예를 들어, (0, 0) 에서 (3, 2) 까지의 +3 변화량을 적용한 2차원 배열을 구하고 싶다면
  - ```plain

    // 아무 변화가 없는 상태
    [ 0, 0, 0, 0 ]
    [ 0, 0, 0, 0 ]
    [ 0, 0, 0, 0 ]
    [ 0, 0, 0, 0 ]
    [ 0, 0, 0, 0 ]


    // 각 행 별로 변화량 누적합을 구할 수 있는 배열
    [ 3, 0, 0, -3 ]
    [ 3, 0, 0, -3 ]
    [ 3, 0, 0, -3 ]
    [ 3, 0, 0, -3 ]
    [ 0, 0, 0, 0 ]
    -> 누적합을 하면 마지막 행을 제외한 각 행은 [3, 3, 3, 0] 이 된다.


    하지만 2차원 배열의 누적합은 열의 방향으로도 이루어지므로 열의 방향에 대한 변화량도 구할 수 있어야 한다.


    [ 3, 3, 3, 0 ]
    [ 0, 0, 0, 0 ]
    [ 0, 0, 0, 0 ]
    [ 0, 0, 0, 0 ]
    [ -3, -3, -3, 0 ]
    -> 위 행렬을 위에서 아래로 누적합을 하면 각 열은 [3, 3, 3, 0] 이 된다.


    // 위 2가지 아이디어를 종합하면 최종적으로 아래 배열의 형태에서 누적합을 구하면 (0,0) 에서 (3,2) 구간까지 변화량에 대한 누적합 배열을 구할 수 있다.
    [ 3, 0, 0, -3 ]
    [ 0, 0, 0, 0 ]
    [ 0, 0, 0, 0 ]
    [ 0, 0, 0, 0 ]
    [ -3, 0, 0, 3 ]


    // 먼저 각 행의 왼쪽에서 오른쪽으로 누적합을 구한다.
    [ 3, 3, 3, 0 ]
    [ 0, 0, 0, 0 ]
    [ 0, 0, 0, 0 ]
    [ 0, 0, 0, 0 ]
    [ -3, -3, -3, 0 ]


    // 이후 각 열의 위에서 아래로 누적합을 구한다.
    [ 3, 3, 3, 0 ]
    [ 3, 3, 3, 0 ]
    [ 3, 3, 3, 0 ]
    [ 3, 3, 3, 0 ]
    [ 0, 0, 0, 0 ]

    -> (0,0) 에서 (3, 2) 까지의 구간에서 +3 만큼의 변화량이 적용된 누적합 배열
    ```

- 누적합 배열로 답을 구하면 완전탐색으로 풀이했을 때 `O(n * m k(skill 길이))` 의 복잡도에서 `O(k + n * m)` 으로 줄일 수 있다.
  - skill을 순회하는 연산에서 `O(k)`
  - 누적합 배열을 구하고 board에서 계산하는 연산에서 2차원 배열이므로 `O(n * m)`
    - 누적합 배열을 구할 때 행에서 한 번, 열에서 한 번, 그리고 각 board의 원소를 순회하면서 계산할 때 한 번이므로 정확히는 `O(3 * n * m)` 이지만 3은 생략

```python
# 누적합을 이용한 풀이
def solution(board, skill):
    answer = 0
    N, M = len(board), len(board[0])
    prefix_sum = [[0] * (M + 1) for _ in range(N + 1)]

    for typ, r1, c1, r2, c2, degree in skill:
        if typ == 1:
            degree = -degree
        # (r1, c1) 위치에 n, (r1, c2 + 1) 위치에 -n
        prefix_sum[r1][c1] += degree
        prefix_sum[r1][c2 + 1] -= degree

        # (r2 + 1, c1) 위치에 -n, (r2 + 1, c2 + 1) 위치에 n
        prefix_sum[r2 + 1][c1] -= degree
        prefix_sum[r2 + 1][c2 + 1] += degree

    for i in range(N + 1):
        for j in range(1, M + 1):
            prefix_sum[i][j] += prefix_sum[i][j - 1]

    for k in range(M + 1):
        for h in range(1, N + 1):
            prefix_sum[h][k] += prefix_sum[h - 1][k]

    for r in range(N):
        for c in range(M):
            board[r][c] += prefix_sum[r][c]
            if board[r][c] > 0:
                answer += 1
    return answer
```
