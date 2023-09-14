# 문제

https://www.acmicpc.net/problem/1504

# 풀이

- 다익스트라 문제
- 고려해야 하는 케이스
  - case1) 출발지 -> v1 -> v2 -> 목적지
  - case2) 출발지 -> v2 -> v1 -> 목적지
  - 출발지는 항상 1이고, 목적지는 항상 N

```python
import sys
input = sys.stdin.readline


MAX_VALUE = 1001 * 800 * 200000


def djikstra(N, E, graph, s, e):
    dist = [MAX_VALUE] * (N + 1)
    visited = [False] * (N + 1)
    dist[s] = 0

    for _ in range(E + 1):
        minI = -1
        minV = MAX_VALUE
        for i in range(1, N + 1):
            if not visited[i] and dist[i] < minV:
                minI = i
                minV = dist[i]
        visited[minI] = True
        if minI == e:
            break

        for v, d in graph[minI]:
            if not visited[v] and dist[v] > dist[minI] + d:
                dist[v] = dist[minI] + d
    if not visited[e]:
        return MAX_VALUE

    return dist[e]


N, E = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(E):
    s, e, d = map(int, input().split())
    graph[s].append((e, d))
    graph[e].append((s, d))

v1, v2 = map(int, input().split())

answer = MAX_VALUE

# s -> v1 -> v2 -> e
from_s_to_v1 = djikstra(N, E, graph, 1, v1)
from_v1_to_v2 = djikstra(N, E, graph, v1, v2)
from_v2_to_e = djikstra(N, E, graph, v2, N)
ans1 = from_s_to_v1 + from_v1_to_v2 + from_v2_to_e

# s -> v2 -> v1 -> e
from_s_to_v2 = djikstra(N, E, graph, 1, v2)
from_v2_to_v1 = djikstra(N, E, graph, v2, v1)
from_v1_to_e = djikstra(N, E, graph, v1, N)
ans2 = from_s_to_v2 + from_v2_to_v1 + from_v1_to_e

answer = min(answer, ans1, ans2)
if answer == MAX_VALUE:
    print(-1)
else:
    print(answer)

```
