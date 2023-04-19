import sys
from collections import deque
input = sys.stdin.readline

def unify(boards, pos):
    # 현재 pos 위치의 모든 파이어볼 합치기
    # 합치면서 방향 체크(모두 홀수이거나 짝수이면 0, 2, 4, 6  | 아니라면 1, 3, 5, 7)
    # next_d가 0이면 다음 방향은 0 2 4 6, 1이면 1 3 5 7
    pos_r, pos_c = pos
    total_m, total_s = 0, 0
    isOdd = True
    isEven = True

    while boards[pos_r][pos_c]:
        fire_m, fire_s, fire_d = boards[pos_r][pos_c].pop()
        total_m += fire_m
        total_s += fire_s
        if fire_d % 2:
            isEven = False
        else:
            isOdd = False
        
    if not isEven and not isOdd:                                # 모두 홀수이거나 모두 짝수인 경우가 아님
        next_d = 1
    else:
        next_d = 0

    return  total_m, total_s, next_d


def divide(pos, total_m, total_s, next_d, cnt, fireballs):
    r, c = pos
    next_m = total_m // 5
    next_s = total_s // cnt
    
    if next_m == 0:
        return 
    
    if next_d == 0:
        d = [0, 2, 4, 6]
    else:
        d = [1, 3, 5, 7]
    
    for i in range(4):
        fireballs.append((r, c, next_m, next_s, d[i]))
    return


N, M, K = map(int, input().split())
boards = [[[] for _ in range(N + 1)] for _ in range(N + 1)]     # [(질량, 속력, 방향)]
fireballs = deque()

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireballs.append((r, c, m, s, d))

dirs = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]   # 방향

while K > 0:
    while fireballs:
        r, c, m, s, d = fireballs.popleft()                                     # 파이어볼 이동
        nr, nc = (r + dirs[d][0] * s) % N, (c + dirs[d][1] * s) % N             # 1번과 N번이 연결되어있기 때문
        boards[nr][nc].append((m, s, d))
    
    for r in range(N):
        for c in range(N):
            if len(boards[r][c]) == 0:
                continue
            if len(boards[r][c]) >= 2:
                cnt = len(boards[r][c])
                tm, ts, nd = unify(boards, (r, c))
                divide((r, c), tm, ts, nd, cnt, fireballs)
            else:
                m, s, d = boards[r][c].pop()
                fireballs.append((r, c, m, s, d))
    K -= 1

answer = 0
while fireballs:
    ball = fireballs.popleft()
    answer += ball[2]
print(answer)
