from collections import deque

"""
BFS 탐색 + 석유량 합 계산
"""
def get_oil(land, head_table, start):
    result = 0
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상, 하, 좌, 우
    
    q = deque([start])
    head_table[start[0]][start[1]] = start
    result += 1
    while len(q) > 0:
        r, c = q.popleft()
        for dr, dc in delta:
            nr, nc = (r + dr, c + dc)
            if 0 <= nr < len(land) and 0 <= nc < len(land[0]) and not head_table[nr][nc]:
                if not land[nr][nc]:
                    continue
                head_table[nr][nc] = (start[0], start[1])
                result += 1
                q.append((nr, nc))
                
            
    return result


def solution(land):
    table = [0] * len(land[0]) # 열 석유량 기록 테이블
    head_table = [[None for c in range(len(land[0]))] for r in range(len(land))] # 지도의 각 노드 별 head 좌표 기록 테이블
    oil_map = {} # head 노드를 key로 하고, 해당 노드를 통해 채굴 가능한 석유량 기록
    
    # 열 -> 행 별로 탐색
    for j in range(len(land[0])):
        oil_empty = []  # 이미 시추를 끝낸 영역의 head 노드를 기록하는 배열
        
        for i in range(len(land)):
            if not land[i][j] or head_table[i][j] in oil_empty:
                continue
            if head_table[i][j]: # 현재 위치에 head 노드가 이미 기록되어 있다면
                head_r, head_c = head_table[i][j]  
                table[j] += oil_map.get((head_r, head_c)) # head 노드로 시추 가능한 석유량을 기록한 테이블에서 값을 구한 후에 누적
                oil_empty.append((head_r, head_c)) # 현재 열에서 해당 head 노드의 영역에 대해 시추를 끝냈으므로 oil_empty에 기록
                continue
            result = get_oil(land, head_table, (i, j))
            table[j] += result
            oil_map[(i, j)] = result
            oil_empty.append((i, j))
    return max(table)