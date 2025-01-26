from collections import deque

'''
그래프 탐색 함수
'''


def search(start: int):
    global table, routes, answer

    q = deque([start])
    visited = set()

    while q:
        node = q.popleft()

        for next_node in routes[node]:
            # fan in이 1 이상이고 fan out이 0이라면 그래프의 끝점이므로 막대 그래프 개수 + 1을 한 후에 해당 그래프 영역은 더이상 방문하지 않는다.
            if table[next_node][0] >= 1 and table[next_node][1] == 0:
                answer[2] += 1
                continue

            # fan in이 2 이상이고 fan out이 2라면 8자 모양 그래프의 중심 노드이므로 8자 모양 그래프 개수 + 1
            if table[next_node][0] >= 2 and table[next_node][1] == 2:
                answer[3] += 1
                continue

            # 방문했던 점으로 다시 돌아왔다면 도넛 모양 그래프 개수 + 1
            if next_node in visited:
                answer[1] += 1
                continue

            q.append(next_node)
            visited.add(next_node)

    return


'''
각 모양 별 중심 노드

도넛 모양 그래프: fan in 최소 1개, fan out 1개, 시작점과 끝점이 같음
막대 모양 그래프: fan in 최소 0개, fan out 1개 혹은 fan in 최소 1개, fan out 0개, 시작점과 끝점이 다름
8자 모양 그래프: fan in 최소 2개, fan out 2개

새로 생성한 노드는 fan in 0개, fan out 1개 이상
'''


def solution(edges):
    global table, routes, answer
    answer = [0, 0, 0, 0]
    # 노드 별 [fan in, fan out] 카운트 기록 테이블
    table = [[0, 0] for _ in range(1000001)]
    routes = [[] for _ in range(1000001)]            # 노드 별 경로를 저장하는 테이블

    for source, target in edges:
        table[source][1] += 1   # fan out
        table[target][0] += 1   # fan in
        routes[source].append(target)   # 단방향 연결

    # fan in은 0이고 fan out이 2 이상인 노드가 새로 생성한 노드(각 그래프 합의 수가 2 이상이므로 새로 생성한 노드의 fan out은 2 이상이어야 함)
    start_node = 0
    for idx, node in enumerate(table):
        if node[0] == 0 and node[1] >= 2:
            start_node = idx
            answer[0] = idx
            break

    search(start_node)
    return answer
