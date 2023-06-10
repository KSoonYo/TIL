

def stars(s, paper, k):
    r, c = s
    jump = k // 3 

    if k == 3:
        for i in range(r, r + 3):
            for j in range(c, c + 3):
                if i == r + jump and j == c + jump:
                    continue
                paper[i][j] = '*'
        return

    for i in range(r, r + k, jump):
        for j in range(c, c + k, jump):
            if r + jump <= i < r + jump * 2 and c + jump <= j < c + jump * 2:
                continue
            stars((i, j), paper, jump)
    return



N = int(input())
paper = [[' '] * N for _ in range(N)]
stars((0, 0), paper, N)
for i in range(N):
    for j in range(N):
        print(paper[i][j], end='')
    print()