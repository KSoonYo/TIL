# 누적합을 이용한 풀이
def solution(board, skill):
    answer = 0
    N, M = len(board), len(board[0])
    prefix_sum = [[0] * (M + 1) for _ in range(N + 1)]
    
    for typ, r1, c1, r2, c2, degree in skill:
        if typ == 1:
            degree = -degree
        # (r1, c1) 위치에 n, (r1, c2 + 1) 위치에 -n
        prefix_sum[r1][c1] += degree
        prefix_sum[r1][c2 + 1] -= degree
        
        # (r2 + 1, c1) 위치에 -n, (r2 + 1, c2 + 1) 위치에 n
        prefix_sum[r2 + 1][c1] -= degree
        prefix_sum[r2 + 1][c2 + 1] += degree

    for i in range(N + 1):
        for j in range(1, M + 1):
            prefix_sum[i][j] += prefix_sum[i][j - 1]
    
    for k in range(M + 1):
        for h in range(1, N + 1):
            prefix_sum[h][k] += prefix_sum[h - 1][k]
    
    for r in range(N):
        for c in range(M):
            board[r][c] += prefix_sum[r][c]
            if board[r][c] > 0:
                answer += 1
    return answer