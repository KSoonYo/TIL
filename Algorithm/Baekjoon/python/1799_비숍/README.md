# 문제

https://www.acmicpc.net/problem/1799

# 풀이

- 전형적인 백트래킹 혹은 dfs 문제
- 문제에서 비숍은 대각선 방향으로 영향을 끼치는 것에 유의
  - 즉 바로 옆에 있는 비숍은 서로 영향을 받지 않는다.
- 대각선 방향에 비숍이 없어야 하는 것이 문제의 조건
  - 처음부터 모든 대각선에 대해 탐색하려고 하면 시간초과
  - 왼쪽에서 오른쪽 아래 방향, 오른쪽에서 왼쪽 아래 방향으로 2가지 방향으로 나누어 체스판에 둘 수 있는 비숍의 개수를 count한다.
- **(0,0)에 비숍을 둔다고 가정할 때**,
  - 왼쪽에서 오른쪽 아래 방향으로는 (1, 1), (2, 2) ...
  - 이때 col - row의 값이 똑같다.
- **(2,2)에 비숍을 둔다고 가정할 때**,
  - 오른쪽에서 왼쪽 아래 방향으로는 (3, 1), (4, 0) ...
  - 이때 row + col 값이 똑같다.
- 이를 통해 현재 위치에서 왼쪽에서 오른쪽 아래 방향에 비숍이 있는지 여부는 **1차원 배열에서 (col - row)번째 인덱스의 값이 `True`인지 여부로 알 수 있다.(반대 방향은 row + col)**
  - 따라서 두 개의 배열을 준비하여 현재 위치에 비숍을 둘 수 있는지, 즉 현재 위치의 양 대각선 방향에 비숍이 있는지 여부를 확인한다.
  - 이때 col - row는 음수가 나올 수 있으므로 이를 방지하고자 N - 1를 더하여 (col - row + N - 1)의 꼴을 취한다.
- 가장 첫 줄의 체스판에서 시작하여 탐색
  - (0,0)과 (0,1)에 먼저 비숍을 둘 수 있는지 여부를 체크하고 비숍을 먼저 둔다.(바로 옆에 있는 비숍은 서로 영향을 받지 않으므로)
  - col에 2씩 더하여 대각선 방향으로 영향을 받는 비숍에 대해서만 탐색 + 백트래킹을 한다.
  - 체스판을 흑백으로 보면 더 쉽다.

```python
import sys
input = sys.stdin.readline


N = int(input())
# N의 최대 크기가 10이므로 넉넉하게 최대 크기 * 2 # 왼쪽에서 오른쪽으로 내려가는 대각선
left_to_right = [False] * 21
right_to_left = [False] * 21    # 오른쪽에서 왼쪽으로 내려가는 대각선

MAP = [list(map(int, input().split())) for _ in range(N)]
max1 = 0
max2 = 0


def check(N, MAP, r, c, order, cnt=0):
    global max1, max2
    if c >= N:
        if c % 2 == 0:
            c = 1
        else:
            c = 0
        r += 1

    if r >= N:
        if order:
            max1 = max(cnt, max1)
        else:
            max2 = max(cnt, max2)
        return

    if MAP[r][c] and not left_to_right[c - r + N + 1] and not right_to_left[r + c]:
        left_to_right[c - r + N + 1] = True
        right_to_left[r + c] = True
        MAP[r][c] = 0
        check(N, MAP, r, c + 2, order, cnt + 1)
        left_to_right[c - r + N + 1] = False
        right_to_left[r + c] = False
        MAP[r][c] = 1
    check(N, MAP, r, c + 2, order, cnt)                     # 그냥 지나가는 경우
    return


result = 0
check(N, MAP, 0, 0, 0)
check(N, MAP, 0, 1, 1)
result = max1 + max2
print(result)

```
