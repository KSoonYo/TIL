'''
fail(시간 초과)

heapq로 다익스트라 구현하여 제출했으나 시간 초과

무엇보다도 문제의 조건에 따라 정점의 비용이 음수일 수 있으므로 다익스트라 풀이가 적합하지 않음(물론 사이클이 존재하지 않는 삼각 그래프이므로 다익스트라 풀이가 아예 안되진 않을 듯?)

벨만 포드 알고리즘 등 음수를 허용하는 알고리즘 + 시간 초과를 줄일 수 있는 방법 고민 -> 플로이드 워셜 적용해봐야 할 듯? -> 입력 조건을 보면 절대 못함

'''

import heapq


def dijkstra(graph):
    global dirs, dirs_table

    # 2차원 그래프 노트를 1차원으로 평탄화(기준 길이는 3)
    dist = [float('INF')] * (len(graph) * 3)
    dist[1] = graph[0][1]
    q = [(dist[1], 1)]  # (cost, node)

    while q:
        cost, node = heapq.heappop(q)   # 최소힙 이용

        if dist[node] < cost:
            continue

        r, c = node // 3, node % 3
        ndirs = dirs_table[c]
        for ndir_idx in ndirs:
            nr, nc = r + dirs[ndir_idx][0], c + dirs[ndir_idx][1]
            flat = nr * 3 + nc
            if 0 <= nr < len(graph) and 0 <= nc < 3 and dist[flat] >= cost + graph[nr][nc]:
                ncost = cost + graph[nr][nc]
                dist[flat] = ncost
                heapq.heappush(q, (ncost, flat))

    return dist[len(graph) * 3 - 2]


# [오른쪽, 아래, 오른쪽 아래 대각선, 왼쪽 아래 대각선]
dirs = [(), (0, 1), (1, 0), (1, 1), (1, -1)]

dirs_table = {
    0: [1, 2, 3],
    1: [1, 2, 3, 4],
    2: [2, 4]
}


flag = False
tc_num = 1
results = []
while not flag:
    tc = int(input())
    if tc == 0:
        flag = True
        break

    graph = []
    for _ in range(tc):
        row = list(map(int, input().split()))
        graph.append(row)

    result = dijkstra(graph)

    results.append(f'{tc_num}. {result}')
    tc_num += 1

for result in results:
    print(result)
