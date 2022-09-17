# example.py
from collections import deque

def search_0_1_bfs(graph, n):

    dist = [float('inf')] * (n + 1)
    dist[1] = 0
    q = deque([(2, 1), (3, 0)])
    while q:
        here, weight = q.popleft()
        
        for next, next_weight in graph[here]:
            if dist[next] > weight + next_weight:
                dist[next] = weight + next_weight
                if next_weight:
                    q.append((next, weight + next_weight))
                else:
                    q.appendleft((next, weight + next_weight))
    
    print(dist[1:]) # output : [0, 1, 0, 0, 1, 1, 2]

n = 7
graph = [  
    0, [(2, 1), (3, 0)], [(1, 1), (4, 1), (7, 1)],
    [(1, 0), (4, 0)], [(3, 0), (2, 1), (5, 1)], 
    [(4, 1), (6, 0)], [(5, 0), (7, 1)], [(2, 1), (6, 1)]
]

search_0_1_bfs(graph, n) 