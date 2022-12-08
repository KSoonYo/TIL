# 플로이드 워셜

- 모든 노드 대 모든 노드 간 최단 거리 알고리즘
- 그래프에서 가능한 모든 노드 쌍에 대해 최단 거리를 구하는 알고리즘
- 다익스트라와 달리 모든 노드 쌍에 대해 최단 거리를 구하고, 음의 가중치를 가지는 그래프에서도 쓸 수 있다.
- O(n^3)
- i 노드에서 j 노드로 가는 경로의 거리가, 중간에 node를 거쳐서 지나갈 때보다 큰 경우, 거리 값을 최소로 갱신
- example

  ```python
  # node의 개수가 4개인 경우, 간선 그래프

  # 양방향 그래프
  graph = [
      [0, 2, 5, 1],
      [2, 0, 7, 11],
      [5, 7, 0, 4],
      [1, 11, 4, 0]
    ]

  # 단방향 그래프
  graph = [
      [0, 2, 5, 1],
      [1, 0, 4, 11],
      [3, 10, 0, 6],
      [20, 12, 9, 0]
    ]


  for node in range(4):
      for i in range(4):
          for j in range(4):
              if graph[i][j] > graph[i][node] + graph[node][j]:
                  graph[i][j] = graph[i][node] + graph[node][j]
  print(graph)

  '''
  양방향 그래프: [
    [0, 2, 5, 1],
    [2, 0, 7, 3],
    [5, 7, 0, 4],
    [1, 3, 4, 0]
  ]

  단방향 그래프: [
    [0, 2, 5, 1],
    [1, 0, 4, 2],
    [3, 5, 0, 4],
    [12, 12, 9, 0]
  ]
  '''
  ```

## 응용문제) 백준 11265 끝나지 않는 파티

[링크](https://www.acmicpc.net/problem/11265)

- 플로이드 워셜을 이용한 풀이

```python
def Floyd_warshall(N, MAP):
    for node in range(N):
        for i in range(N):
            for j in range(N):
                if MAP[i][j] > MAP[i][node] + MAP[node][j]:
                    # i에서 j까지 가는 길 거리가 node를 거쳐서 지나갈 때보다 큰 경우 -> 거리 갱신
                    MAP[i][j] = MAP[i][node] + MAP[node][j]

    return

N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

Floyd_warshall(N, MAP)

for _ in range(M):
    s, e, c = map(int,input().split())
    if MAP[s-1][e-1] > c:
        print('Stay here')
    else:
        print('Enjoy other party')
```

- heapq와 다익스트라를 이용한 풀이

```python
import sys, heapq
input = sys.stdin.readline


def dijk(s):
    cost = [500000001] * N
    cost[s] = 0
    heap = [[0, s]]
    visited = [0] * N

    while heap:
        c, idx = heapq.heappop(heap)
        if visited[idx]:
            continue

        visited[idx] = 1
        for i in range(N):
            if not visited[i] and c + lines[idx][i] < cost[i]:
                cost[i] = c + lines[idx][i]
                heapq.heappush(heap, [c + lines[idx][i], i])

    return cost


N, M = map(int, input().split())
lines = [list(map(int, input().split())) for _ in range(N)]
costs = []
for i in range(N):
    costs.append(dijk(i))

answer = []
for i in range(M):
    A, B, C = map(int, input().split())
    if costs[A - 1][B - 1] > C:
        answer.append('Stay here\n')
    else:
        answer.append('Enjoy other party\n')

print(''.join(answer))

```
