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


