import sys

input = sys.stdin.readline

def find(v):
    if parents[v] == v:
        return v
    parents[v] = find(parents[v])
    return parents[v]

def union(u, v):
    u = find(u)
    v = find(v)
    parents[u] = v
    return

N = int(input())
M = int(input())
cities = [[0] * (N + 1)]
parents = [i for i in range(N + 1)]
for _ in range(N):
    cities.append([0] + list(map(int, input().split())))

routes = list(map(int, input().split()))
    
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if cities[i][j]:
            union(i, j)

parents_set = set(find(parents[rep]) for rep in routes)
if len(parents_set) == 1:
    print('YES')
else:
    print('NO')