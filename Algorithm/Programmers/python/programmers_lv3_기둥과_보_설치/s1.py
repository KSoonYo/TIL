def command(n, build_frame, MAP):
    for x, y, a, b in build_frame:
        target = (y, x)
        if b:
            install(MAP, n, a, target)
        else:
            delete(MAP, n, a, target)

    return get_answer(n, MAP)
    
def install(MAP, n, typ, target):
    r, c = target                       # 지정된 좌표 위치(기둥의 아래 부분 or 보의 왼쪽 부분)
    if typ:                             # 보 설치
        if r > 0 and (MAP[r - 1][c] & (1 << 0) or (MAP[r - 1][c + 1] & (1 << 0)) or (MAP[r][c - 1] & (1 << 1) and MAP[r][c + 1] & (1 << 1))):
            MAP[r][c] |= (1 << 1)
        
    else:                               # 기둥 설치
        if r == 0 or (MAP[r][c] & (1 << 1)) or (MAP[r][c - 1] & (1 << 1)) or (MAP[r - 1][c] & (1 << 0)):
            MAP[r][c] |= (1 << 0)

def delete(MAP, n, typ, target):
    r, c = target

    if typ:                             # 보 삭제
        MAP[r][c] &= ~(1 << 1)
    else:                               # 기둥 삭제
        MAP[r][c] &= ~(1 << 0)
    
    if not check(n, MAP):       # 조건에 부합하지 않으면 원상복구
        if typ:
            MAP[r][c] |= (1 << 1)
        else:
            MAP[r][c] |= (1 << 0)
    return 

def check(n, MAP):
    for i in range(n + 1):
        for j in range(n + 1):
            if MAP[i][j] & (1 << 0):    # 기둥이 설치되어 있다면
                if i > 0 and (not (MAP[i - 1][j] & (1 << 0)) and (not MAP[i][j - 1] & (1 << 1)) and (not MAP[i][j] & (1 << 1))):
                    return False
            if MAP[i][j] & (1 << 1):    # 보가 설치되어 있다면
                if not MAP[i - 1][j] & (1 << 0) and not MAP[i - 1][j + 1] & (1 << 0) and ((not MAP[i][j - 1] & (1 << 1)) or (not MAP[i][j + 1] & (1 << 1))):
                    return False
    return True

def get_answer(n, MAP, answer = []):
    for i in range(n + 1):
        for j in range(n + 1):
            if not MAP[i][j]:
                continue
            if i + 1 <= n and MAP[i][j] & (1 << 0):
                answer.append([j, i, 0])
            if j + 1 <= n and MAP[i][j] & (1 << 1):
                answer.append([j, i, 1])
    answer.sort(key=lambda x: (x[0], x[1], x[2]))
    return answer

def solution(n, build_frame):
    MAP = [[0] * (n + 1) for _ in range(n + 1)]  # 00: 무설치, 01: 기둥, 10: 보, 11: 기둥 + 보
    # 좌표계를 아래로 반전시켜서 가장 맨 위를 바닥으로 변환    
    return command(n, build_frame, MAP)




## best solution
# 핵심: 삭제 가능한지에 대한 조건을 일단 제거하고 나서 다시 설치 가능한지에 대한 조건으로 변환하여 풀이
def is_installable(x, y, is_beam, beam_board, pillar_board):
    if is_beam:
        return (pillar_board[x][y - 1] or pillar_board[x + 1][y - 1]) or ((x >= 1 and beam_board[x - 1][y]) and beam_board[x + 1][y])
    else:
        return (y == 0) or ((x >= 1 and beam_board[x - 1][y]) or beam_board[x][y]) or pillar_board[x][y - 1]

def install(x, y, is_beam, beam_board, pillar_board, is_install):
    if is_beam:
        beam_board[x][y] = is_install
    else:
        pillar_board[x][y] = is_install

def check_validity(res, beam_board, pillar_board):
    for x, y, is_beam in res:
        if not is_installable(x, y, is_beam, beam_board, pillar_board):
            return False
    return True

def solution(board_sz, insts):
    res = []
    beam_board = [[False] * (board_sz + 1) for _ in range(board_sz + 1)]
    pillar_board = [[False] * (board_sz + 1) for _ in range(board_sz + 1)]
    for x, y, is_beam, is_install in insts:
        if is_install:
            if is_installable(x, y, is_beam, beam_board, pillar_board):
                install(x, y, is_beam, beam_board, pillar_board, is_install)
                res.append([x, y, is_beam])
        else:
            install(x, y, is_beam, beam_board, pillar_board, is_install)
            if check_validity(res, beam_board, pillar_board):
                res.remove([x, y, is_beam])
            else:
                install(x, y, is_beam, beam_board, pillar_board, True)
    return sorted(res)