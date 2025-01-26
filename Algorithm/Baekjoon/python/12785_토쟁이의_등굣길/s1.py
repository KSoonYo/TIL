'''
fail

집 -> 토스트 와 토스트 -> 학교를 구분해서 생각하는 아이디어는 맞았으나, 구현 방법이 틀림

목적지 (i, j) 지점까지 도달 가능한 경로 개수를 dp로 메모하여 풀이해야 함
이때 시작지점에서 왼 -> 오, 위 -> 아래 방향으로 가는 것이 목적지까지의 최소 경로를 보장
'''

from collections import deque


def search(start, end, my_map, goal="toast"):
    global to_toast_routes, to_school_routes, w, h, dirs

    q = deque([(start, 0)])  # (node, cost)
    my_map[start[0]][start[1]] = 0
    minimal_cost = None

    while q:
        node, cost = q.popleft()
        r, c = node

        # 이미 도착했고, 더 비용이 큰 경로에 대해서는 무시
        if minimal_cost and cost > minimal_cost:
            return

        if node == end:
            if not minimal_cost:
                minimal_cost = cost
            if goal == 'toast':
                to_toast_routes += 1
            elif goal == 'school':
                to_school_routes += 1
            continue

        for r_dir, c_dir in dirs:
            nr, nc = r + r_dir, c + c_dir
            if start[0] <= nr <= end[0] and start[1] <= nc <= end[1]:
                if my_map[nr][nc] > cost + 1:
                    my_map[nr][nc] = cost + 1
                    q.append(((nr, nc), cost + 1))
                elif (nr, nc) == end:
                    q.append(((nr, nc), my_map[nr][nc]))
    return


w, h = map(int, input().split())

x, y = map(int, input().split())
my_first_map = [[float('inf')] * (w + 1) for _ in range(h + 1)]
my_second_map = [[float('inf')] * (w + 1) for _ in range(h + 1)]

dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

to_toast_routes = 0
to_school_routes = 0

search((1, 1), (y, x), my_first_map)
search((y, x), (h, w), my_second_map,  'school')
print(to_toast_routes * to_school_routes % 1000007)
