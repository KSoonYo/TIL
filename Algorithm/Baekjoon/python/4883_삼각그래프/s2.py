
# [오른쪽, 아래, 오른쪽 아래 대각선, 왼쪽 아래 대각선]
dirs = [(), (0, 1), (1, 0), (1, 1), (1, -1)]

dirs_table = {
    0: [2, 4],
    1: [1, 2, 3, 4],
    2: [1, 2, 3]
}   # 노드에 도달할 수 있는(fan-in) 방향의 가짓수


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

    # dp[i] : i번째 노드에 도달하는 데 필요한 최소 비용
    dp = [float('INF')] * len(graph) * 3    # 0번 노드부터 시작
    dp[1] = graph[0][1]
    dp[2] = graph[0][1] + graph[0][2]

    for node in range(3, len(graph) * 3):
        r, c = node // 3, node % 3  # 2차원 그래프 (행, 열)로 변환
        selected_dirs = dirs_table[c]

        candidates = [dp[node]]
        for idx in selected_dirs:
            selected_dir = dirs[idx]
            source_r, source_c = r - \
                selected_dir[0], c - selected_dir[1]  # - 부호로 방향의 역전
            source_node = source_r * 3 + source_c

            dp[node] = min(dp[node], graph[r][c] + dp[source_node])

    results.append(f'{tc_num}. {dp[len(graph) * 3 - 2]}')
    tc_num += 1

for result in results:
    print(result)
