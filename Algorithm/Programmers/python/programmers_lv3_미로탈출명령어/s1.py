import sys
sys.setrecursionlimit(5000)

def search(n, m, k, s, e, p, temp=''):
    # 일단 사전 순대로의 방향으로 이동해서 탈출이 가능한지 여부를 체크(그리디 + DFS)
    dirs = [['d', 1, 0], ['l', 0, -1], ['r', 0, 1], ['u', -1, 0]]                   # 사전 순 방향 (위, 왼, 오, 아래)
    dist = abs(e[0] - p[0]) + abs(e[1] - p[1])                                      # 도착지와 현재 위치 간 거리(맨헤튼 거리)
        
    if k == 0 and p == e:                                                           # 현재 위치가 도착지이고, 이동 횟수를 모두 소모했다면
        return temp                                                                 # 지금까지 쌓인 command 반환
    
    if k < dist or (k - dist) % 2:                                                  # 무슨 이동을 해도 탈출이 불가능하다면
        return                                                                      # back

    
    result = None
    for command, dr, dc in dirs:                                                    
        nr, nc = p[0] + dr, p[1] + dc
        if 0 < nr <= n and 0 < nc <= m:                                             # 다음 위치가 격자를 벗어나지 않는다면
            if abs(e[0] - nr) + abs(e[1] - nc) <= k:                                # 도착지와 다음 위치의 거리가 k 범위 이내라면
                result = search(n, m, k - 1, s, e, (nr, nc), temp + command)        # 현재 command 저장 후 다음 위치에서의 이동 탐색
                if result:                                                          # 반환된 command가 존재하면 break
                    break
    return result

def solution(n, m, x, y, r, c, k):
    answer = search(n, m, k, (x, y), (r, c), (x, y))
    if not answer:
        answer = 'impossible'
    return answer