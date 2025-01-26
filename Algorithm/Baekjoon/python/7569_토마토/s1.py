from collections import deque


def ripen(pos: tuple[int, int]):
    global m, n, h, matrix, recorded_day, unripe_tomato_table, dirs

    t_r, t_c = pos
    q = deque([])  # [((x, y), 숙성일)]
    t_level = t_r // h
    t_offset = t_r % h

    # 해당 토마토의 인근 익지 않은 토마토를 모두 시작 queue에 넣고 숙성 시작
    for t_dr, t_dc in dirs:
        nt_r, nt_c = t_r + t_dr, t_c + t_dc
        nt_level = nt_r // h
        nt_offset = nt_r % h
        if 0 <= nt_r < n * h and 0 <= nt_c < m and matrix[nt_r][nt_c] == 0:
            if t_level == nt_level or t_offset == nt_offset:
                matrix[nt_r][nt_c] = 1
                unripe_tomato_table.discard((nt_r, nt_c))
                q.append(((nt_r, nt_c), 1))

    while q:
        pos, rippen_day = q.popleft()
        r, c = pos
        print('start: ', (r, c))
        recorded_day = max(recorded_day, rippen_day)

        level = r // h  # 상자의 층 수
        offset = r % h  # 층 내 토마토 위치
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            nlevel = nr // h
            noffset = nr % h

            # 인근에 익지 않은 토마토가 있는지 탐색
            if 0 <= nr < n * h and 0 <= nc < m and matrix[nr][nc] == 0:
                if level == nlevel or offset == noffset:
                    print('ripped! ', (nr, nc), 'day: ', rippen_day + 1)
                    matrix[nr][nc] = 1                    # 익은 토마토로 변경
                    # 익지 않은 토마토로 기록되어 있다면 익었으므로 테이블에서 제거
                    unripe_tomato_table.discard((nr, nc))
                    q.append([(nr, nc), rippen_day + 1])
        print(' ----- -------')
    return


'''
Fail

접근 방법이 잘못됨
offset을 적용하여 2차원 탐색을 통해 해결하려 했으나 실패함

'''


def ripen(pos: tuple[int, int]):
    global m, n, h, matrix, recorded_day, unripe_tomato_table, dirs, ripped_day_table

    t_r, t_c = pos
    q = deque([])  # [((x, y), 숙성일)]
    t_level = t_r // n
    t_offset = t_r % n

    # 해당 토마토의 인근 익지 않은 토마토를 모두 시작 queue에 넣고 숙성 시작
    for t_dr, t_dc in dirs:
        nt_r, nt_c = t_r + t_dr, t_c + t_dc
        nt_level = nt_r // n
        nt_offset = nt_r % n
        if 0 <= nt_r < n * h and 0 <= nt_c < m and matrix[nt_r][nt_c] != -1:
            if t_level != nt_level and t_offset != nt_offset:
                continue
            if matrix[nt_r][nt_c] == 0 or ripped_day_table[nt_r][nt_c] > 1:
                ripped_day_table[nt_r][nt_c] = 1
                matrix[nt_r][nt_c] = 1
                unripe_tomato_table.discard((nt_r, nt_c))
                q.append(((nt_r, nt_c), 1))

    while q:
        pos, rippen_day = q.popleft()
        r, c = pos

        level = r // n  # 상자의 층 수
        offset = r % n  # 층 내 토마토 위치
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            nlevel = nr // n
            noffset = nr % n

            # 인근에 익지 않은 토마토가 있는지 탐색
            if 0 <= nr < n * h and 0 <= nc < m and matrix[nr][nc] != -1:
                if level != nlevel or offset != noffset:
                    continue
                if matrix[nr][nc] == 0 or ripped_day_table[nr][nc] > rippen_day + 1:
                    ripped_day_table[nr][nc] = rippen_day + 1
                    recorded_day = rippen_day + 1
                    matrix[nr][nc] = 1                     # 익은 토마토로 변경

                    # 익지 않은 토마토로 기록되어 있다면 익었으므로 테이블에서 제거
                    unripe_tomato_table.discard((nr, nc))
                    q.append([(nr, nc), rippen_day + 1])

    return


m, n, h = list(map(int, input().split()))

matrix = [list(map(int, input().split())) for _ in range(n * h)]
ripped_day_table = [[9876543210] * m for _ in range(n * h)]
unripe_tomato_table = set()   # 아직 익지 않은 토마토를 기록하는 테이블

recorded_day = 0

dirs = [(1, 0), (-1, 0), (0, -1), (0, 1), (-h, 0), (h, 0)]  # 앞, 뒤, 왼, 오, 위, 아래

for r in range(n * h):
    for c in range(m):
        if matrix[r][c]:
            continue

        # 현재 위치에서 위, 아래, 앞, 뒤, 왼, 오에서 익은 토마토가 있는지 탐색
        is_rippen_tomato = False

        level = r // h  # 상자의 층 수
        offset = r % h  # 층 내 토마토 위치

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            nlevel = nr // h
            noffset = nr % h

            # 인근에 익은 토마토가 있는 경우
            if 0 <= nr < n * h and 0 <= nc < m and matrix[nr][nc] == 1:
                if level == nlevel or offset == noffset:
                    is_rippen_tomato = True
                    ripen((nr, nc))

        # 인근에 익은 토마토가 없다면, 아직 익지 않은 토마토 테이블에 현재 토마토 위치를 기록
        if not is_rippen_tomato:
            unripe_tomato_table.add((r, c))

if len(unripe_tomato_table) > 0:  # 익지 않은 토마토가 남아있다면 -1 출력
    print(-1)
else:
    print(recorded_day)
dirs = [(1, 0), (-1, 0), (0, -1), (0, 1), (-h, 0), (h, 0)]  # 앞, 뒤, 왼, 오, 위, 아래

for r in range(n * h):
    for c in range(m):
        if matrix[r][c]:  # 익은 토마토 혹은 토마토가 없는 위치에 대해서는 탐색 x
            continue

        # 현재 위치에서 위, 아래, 앞, 뒤, 왼, 오에서 익은 토마토가 있는지 탐색
        is_rippen_tomato = False

        level = r // n  # 상자의 층 수
        offset = r % n  # 층 내 토마토 위치 행

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            nlevel = nr // n
            noffset = nr % n

            # 인근에 익은 토마토가 있는 경우
            if 0 <= nr < n * h and 0 <= nc < m and matrix[nr][nc] == 1:
                if level == nlevel or offset == noffset:
                    is_rippen_tomato = True
                    ripen((nr, nc))

        # 인근에 익은 토마토가 없다면, 익지 않은 토마토 테이블에 현재 토마토 위치를 기록
        if not is_rippen_tomato:
            unripe_tomato_table.add((r, c))

if len(unripe_tomato_table) > 0:  # 익지 않은 토마토가 남아있다면 -1 출력
    print(-1)
else:
    print(recorded_day)
