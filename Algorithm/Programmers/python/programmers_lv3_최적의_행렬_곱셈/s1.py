def solution(matrix_sizes):
    answer = 0
    n = len(matrix_sizes)
    table = [[[] for _ in range(n)] for _ in range(n)]

    for i in range(n):                                      # 대각선 행렬 채우기
        x, y = 0, i
        for _ in range(n - i):
            if x == y:
                table[x][y] = (0, matrix_sizes[y])          # (연산 횟수, 현재 행렬)
                x, y = x + 1, y + 1
                continue
            if y - x == 1:
                a, b = table[x][y - 1][1], table[x + 1][y][1]
                c = (a[0] * a[1] * b[1], [a[0], b[1]])
                table[x][y] = c
                x, y = x + 1, y + 1
                continue
            for k in range(1, y - x + 1):
                a, b = table[x][y - k][1], table[y - k + 1][y][1]
                c = (table[x][y - k][0] + table[y - k + 1][y][0] + (a[0] * a[1] * b[1]), [a[0], b[1]])
                if table[x][y]:
                    prev = table[x][y]
                    table[x][y] = (min(prev[0], c[0]), c[1])
                else:
                    table[x][y] = c
            x, y = x + 1, y + 1
    answer = table[0][n - 1][0]
    return answer