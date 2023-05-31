# 문제
https://www.acmicpc.net/problem/1987

# 풀이
- DFS 풀이
- 일반적인 DFS 풀이와 같지만, 핵심은 visited의 배열을 'A' ~ 'Z' 길이까지 정의하고, 깊이 우선 탐색을 하면서 각각의 알파벳 자리를 방문체크와 체크해제를 반복
  - 2차원 visited 배열을 선언해서 사용하거나 list(혹은 문자열)로 path 정보를 매번 체크하면 시간초과
  - set으로 path체크를 하면 메모리 초과 우려
- 알파벳의 인덱스는 ord()로 구한 알파벳의 아스키코드 값 - 65 
  - 'A'의 아스키코드가 65이기 때문
- pypy3으로 통과
```python
import sys
input = sys.stdin.readline


# pypy3 통과

def dfs(R, C, board, pos, cnt = 1):
    global maxV
    r, c = pos
    if cnt > maxV:
        maxV = cnt

    for ndir in dirs:
        nr, nc = r + ndir[0], c + ndir[1]
        if 0 <= nr < R and 0 <= nc < C and not visited[ord(board[nr][nc]) - 65]:
            visited[ord(board[nr][nc]) - 65] = True
            dfs(R, C, board, (nr, nc), cnt + 1)
            visited[ord(board[nr][nc]) - 65] = False
    return



R, C = map(int, input().split())
board = []
for _ in range(R):
    board.append(input().strip())


visited = [False] * 26

dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]   # 상, 하, 좌, 우
start = board[0][0]
maxV = 1
visited[ord(start) - 65] = True
dfs(R, C, board, (0, 0))
print(maxV)

```

