def solution(dirs):
    answer = 0
    d = {
        "U": [-1, 0], "L": [0, -1],
        "D": [1, 0], "R": [0, 1]
    }
    # bits : 1 -> 상, 10 -> 하, 100 -> 좌, 1000 -> 우
    bits = {
        "U" : 0, "L" : 2,
        "D" : 1, "R" : 3
    }
    pair_bits = {
        "U" : 1, "L" : 3,
        "D" : 0, "R" : 2
    }
    board = [[0] * 11 for _ in range(11)]
    r, c = 5, 5
    for dir in dirs:
        nr, nc = r + d[dir][0], c + d[dir][1]
        if 0 <= nr < 11 and 0 <= nc < 11:            
            if not (board[nr][nc] & (1 << bits[dir])):
                board[nr][nc] |= (1 << bits[dir])           # 다음 지점으로 가는 방향 방문 체크
                board[r][c] |= (1 << pair_bits[dir])        # '길'이므로 양방향 방문 체크(다음 지점으로 가는 방향의 반대 방향으로 이전 지점 방문 체크)
                answer += 1
            r, c = nr, nc
    return answer

## best solution
## set()으로 이전 지점과 다음 지점을 묶어서 하나의 집합으로 관리
def solution(dirs):
    s = set()
    d = {'U': (0,1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    x, y = 0, 0
    for i in dirs:
        nx, ny = x + d[i][0], y + d[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            s.add((x,y,nx,ny))
            s.add((nx,ny,x,y))
            x, y = nx, ny
    return len(s)//2