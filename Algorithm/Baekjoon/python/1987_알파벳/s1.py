import sys
input = sys.stdin.readline


# pypy3 통과

def dfs(R, C, board, pos, cnt = 1):
    global maxV
    r, c = pos
    if cnt > maxV:
        maxV = cnt

    for ndir in dirs:
        nr, nc = r + ndir[0], c + ndir[1]
        if 0 <= nr < R and 0 <= nc < C and not visited[ord(board[nr][nc]) - 65]:
            visited[ord(board[nr][nc]) - 65] = True
            dfs(R, C, board, (nr, nc), cnt + 1)
            visited[ord(board[nr][nc]) - 65] = False
    return



R, C = map(int, input().split())
board = []
for _ in range(R):
    board.append(input().strip())


visited = [False] * 26

dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]   # 상, 하, 좌, 우
start = board[0][0]
maxV = 1
visited[ord(start) - 65] = True
dfs(R, C, board, (0, 0))
print(maxV)
