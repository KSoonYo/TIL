import sys
from collections import deque
input = sys.stdin.readline


def find(node):
    global table
    if table[node] == node:
        return node
    table[node] = find(table[node])
    return table[node]


def union(source, target):
    global table, rank

    u = find(source)
    v = find(target)

    # rank 기법으로 재귀, 시간복잡도 최적화
    if table[u] != table[v]:
        if rank[u] > rank[v]:
            table[v] = u
        elif rank[u] < rank[v]:
            table[u] = v
        else:
            table[u] = v
            rank[v] += 1

    return


def kruskal():
    global edges, sebu_map
    edges.sort(key=lambda x: -x[2])   # 내림차순 정렬(가중치가 큰 것부터)
    for s, e, w in edges:
        if find(s) != find(e):
            union(s, e)
            sebu_map[s].append((e, w))  # (목적지, 가중치)
            sebu_map[e].append((s, w))
    return


N, M = map(int, input().split())
s, e = map(int, input().split())
max_available = float('inf')

sebu_map = [[] for _ in range(N + 1)]
table = [i for i in range(N + 1)]
rank = [0] * (N + 1)
edges = []

for _ in range(M):
    node_s, node_e, cost = map(int, input().split())    # 출발지, 목적지, cost
    edges.append((node_s, node_e, cost))


# 다리의 무게 제한만큼 금빼빼로를 들고 갈 수 있다. -> 출발지에서 목적지까지 다리 무게의 합이 가능한 큰 그래프로 연결되어 있어야 한다.
# 즉 튼튼한 다리로 이어졌을 가능성이 큰 그래프들만 탐색하고자 함
# 가중치가 큰 순서대로 "사이클이 존재하지 않도록" 간선을 잇기 위해 크루스칼 알고리즘 활용
kruskal()

visited = [False] * (N + 1)
visited[s] = True
q = deque([(s, float('inf'))])  # (노드, 빼빼로 무게)
while q:
    node, weight = q.popleft()

    # bfs로 목적지에 처음 도달하기만 하면 이미 해당 경로에서 목적지까지 방문 끝난 셈
    if node == e:
        print(weight)
        exit()

    for target, next_weight in sebu_map[node]:
        if not visited[target]:
            visited[target] = True
            q.append((target, min(weight, next_weight)))


print(0)    # 목적지에 도달하지 못하는 경우에는 0 출력
