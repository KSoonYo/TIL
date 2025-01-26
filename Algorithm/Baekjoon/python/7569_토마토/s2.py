from collections import deque


def rippen(pos: tuple[int, int, int]):
    global m, n, h, dirs, rippen_day_table, answer, unripe_tomato_table

    q = deque([(pos, 0)])  # [((h, r, c), 숙성일)]
    init_h, init_r, init_c = pos
    rippen_day_table[init_h][init_r][init_c] = 0

    while q:
        tomato_pos, rippend_day = q.popleft()
        level, r, c = tomato_pos

        for dh, dr, dc in dirs:
            nh, nr, nc = level + dh, r + dr, c + dc
            # 인근에 아직 익지 않은 토마토 탐색
            if 0 <= nh < h and 0 <= nr < n and 0 <= nc < m and not matrix[nh][nr][nc]:
                if rippen_day_table[nh][nr][nc] > rippend_day + 1:
                    rippen_day_table[nh][nr][nc] = rippend_day + 1

                    # 토마토 숙성 완료 표시
                    unripe_tomato_table.discard((nh, nr, nc))
                    q.append(((nh, nr, nc), rippend_day + 1))


m, n, h = list(map(int, input().split()))

matrix = [[list(map(int, input().split())) for _ in range(n)]
          for _ in range(h)]    # matrix[h][n][m]

rippen_day_table = [[[9876543210] * m for _ in range(n)] for _ in range(h)]
unripe_tomato_table = set()     # 아직 익지 않은 토마토 위치를 기록하는 테이블

dirs = [(1, 0, 0), (-1, 0, 0), (0, -1, 0), (0, 1, 0),
        (0, 0, -1), (0, 0, 1)]  # 아래, 위, 앞, 뒤, 왼, 오

answer = 0

for level in range(h):
    for r in range(n):
        for c in range(m):
            # 익은 토마토 혹은 토마토가 없는 위치에 대해서는 탐색하지 않음
            if matrix[level][r][c]:
                continue

            for dh, dr, dc in dirs:
                nh, nr, nc = level + dh, r + dr, c + dc
                # 인근에 익은 토마토가 있는 경우
                if 0 <= nh < h and 0 <= nr < n and 0 <= nc < m and matrix[nh][nr][nc] == 1:
                    # 해당 위치 토마토를 시작으로 숙성 시작
                    rippen((nh, nr, nc))

            # 현재 토마토가 익지 않았다면, 아직 익지 않은 토마토 테이블에 기록
            if rippen_day_table[level][r][c] == 9876543210:
                unripe_tomato_table.add((level, r, c))


for level in range(h):
    for r in range(n):
        for c in range(m):
            if rippen_day_table[level][r][c] == 9876543210:
                continue
            answer = max(answer, rippen_day_table[level][r][c])

if len(unripe_tomato_table) > 0:
    print(-1)
else:
    print(answer)
