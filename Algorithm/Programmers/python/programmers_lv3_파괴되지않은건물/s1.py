# 효율성 테스트 fail
from collections import deque

def recovery(board, r1, c1, r2, c2, degree, destroyed):
    visited = set()
    q = deque([(r1, c1)])               # [(r, c)]
    visited.add((r1, c1))
    while q:
        pos_r, pos_c = q.popleft()
        board[pos_r][pos_c] += degree
        if board[pos_r][pos_c] > 0 and (pos_r, pos_c) in destroyed:
            destroyed.remove((pos_r, pos_c))
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for dr, dc in dirs:
            nr = pos_r + dr
            nc = pos_c + dc
            if r1 <= nr <= r2 and c1 <= nc <= c2 and (nr, nc) not in visited:
                visited.add((nr, nc))
                q.append((nr, nc))
    return

def destroy(board, r1, c1, r2, c2, degree, destroyed):
    visited = set()
    q = deque([(r1, c1)])               # [(r, c)]
    visited.add((r1, c1))
    while q:
        pos_r, pos_c = q.popleft()
        board[pos_r][pos_c] -= degree
        if board[pos_r][pos_c] <= 0 and (pos_r, pos_c) not in destroyed:
            destroyed.add((pos_r, pos_c))
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for dr, dc in dirs:
            nr = pos_r + dr
            nc = pos_c + dc
            if r1 <= nr <= r2 and c1 <= nc <= c2 and (nr, nc) not in visited:
                visited.add((nr, nc))
                q.append((nr, nc))
    return

def solution(board, skill):
    N, M = len(board), len(board[0])
    destroyed = set()
    for typ, r1, c1, r2, c2, degree in skill:
        if typ == 1:
            destroy(board, r1, c1, r2, c2, degree, destroyed)
        else:
            recovery(board, r1, c1, r2, c2, degree, destroyed)
    answer = N * M - len(destroyed)
    return answer