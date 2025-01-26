import sys
input = sys.stdin.readline


def pipelining(pipe_shape, pos):
    global dir_table, routes, pipe_map, N

    r, c = pos

    # 미는 방향이 무조건 지도의 오른쪽으로만 가기 때문에 파이프의 오른쪽 끝점에 대해서만 체크해주면 된다.
    if r == N - 1 and c == N - 1:
        routes += 1
        return

    # 현재 위치에서 주위 방위 체크
    available_flag = [0, 0, 0]  # [가로, 세로, 대각선]
    if c + 1 < N and not pipe_map[r][c + 1]:
        available_flag[0] += 1

    if r + 1 < N and not pipe_map[r + 1][c]:
        available_flag[1] += 1

    if r + 1 < N and c + 1 < N and not pipe_map[r + 1][c + 1]:
        available_flag[2] += 1

    # 주어진 방향대로 파이프 밀기
    if pipe_shape != 'vertical' and c + 1 < N and not pipe_map[r][c + 1]:
        pipelining('horizon', (r, c + 1))

    if pipe_shape != 'horizon' and r + 1 < N and not pipe_map[r + 1][c]:
        pipelining('vertical', (r + 1, c))

    if r + 1 < N and c + 1 < N and not pipe_map[r][c + 1] and not pipe_map[r + 1][c] and not pipe_map[r + 1][c + 1]:
        pipelining('diagonal', (r + 1, c + 1))

    return


N = int(input())
pipe_map = [list(map(int, input().split())) for _ in range(N)]
routes = 0

pipelining('horizon', (0, 1))
print(routes)
