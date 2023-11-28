import sys
input = sys.stdin.readline


N = int(input())
# N의 최대 크기가 10이므로 넉넉하게 최대 크기 * 2 # 왼쪽에서 오른쪽으로 내려가는 대각선
left_to_right = [False] * 21
right_to_left = [False] * 21    # 오른쪽에서 왼쪽으로 내려가는 대각선

MAP = [list(map(int, input().split())) for _ in range(N)]
max1 = 0
max2 = 0


def check(N, MAP, r, c, order, cnt=0):
    global max1, max2
    if c >= N:
        if c % 2 == 0:
            c = 1
        else:
            c = 0
        r += 1

    if r >= N:
        if order:
            max1 = max(cnt, max1)
        else:
            max2 = max(cnt, max2)
        return

    if MAP[r][c] and not left_to_right[c - r + N + 1] and not right_to_left[r + c]:
        left_to_right[c - r + N + 1] = True
        right_to_left[r + c] = True
        MAP[r][c] = 0
        check(N, MAP, r, c + 2, order, cnt + 1)
        left_to_right[c - r + N + 1] = False
        right_to_left[r + c] = False
        MAP[r][c] = 1
    check(N, MAP, r, c + 2, order, cnt)                     # 그냥 지나가는 경우
    return


result = 0
check(N, MAP, 0, 0, 0)
check(N, MAP, 0, 1, 1)
result = max1 + max2
print(result)
