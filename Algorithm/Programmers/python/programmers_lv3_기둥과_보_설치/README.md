# 문제
https://school.programmers.co.kr/learn/courses/30/lessons/60061

# 풀이
- 구현 문제
- 핵심
  - 문제에 주어진 그림을 상하 반전시켜서 2차원 맵 정의
  - 기둥, 보 설치 및 삭제 조건 판별
  - 기둥, 보 설치 및 삭제 표시
  - 기둥과 보 양 지점을 동시에 게산하려하지 말고, 문제에 주어진 대로 기둥은 위로, 보는 오른쪽으로 설치된다는 전제하에 풀이
    - 기둥의 아래 지점과 보의 왼쪽 지점만 알아도 무방

```python
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

```