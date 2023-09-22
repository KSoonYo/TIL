import heapq


def search(table, rest, k, allow=1, waiting=0, typ=1):
    '''
    table : 테이블
    rest : 할당 가능한 전체 상담원 수
    k : 할당 가능한 타입 유형 수
    allow: 현재 타입에서 할당 가능한 상담원 수
    typ : 타입 유형
    '''
    global answer

    ##
    if k == 0:
        answer = min(answer, waiting)
        return

    for extra in range(rest + 1):
        allocated = []
        temp = 0
        for start, ing in table[typ]:
            # 가장 빨리 상담 끝나는 사람의 끝나는 시간이 대기 중인 상담 신청한 사람의 신청 시간 이전이라면 모두 pop
            while allocated and allocated[0][0] <= start:
                heapq.heappop(allocated)

            # 현재 사람이 가장 빨리 끝나는 사람의 상담이 끝날 때까지 얼마나 기다려야 하는지 계산한 후, 상담원 할당
            if len(allocated) < (allow + extra):
                heapq.heappush(allocated, (start + ing, (start, ing)))
            else:
                prev_e = heapq.heappop(allocated)[0]
                temp += (prev_e - start)
                heapq.heappush(
                    allocated, (start + ing + (prev_e - start), (start + (prev_e - start), ing)))

        search(table, rest - extra, k - 1, 1, waiting + temp, typ + 1)

    return


def solution(k, n, reqs):
    global answer
    answer = 987654321
    table = [[] for _ in range(k + 1)]
    rest = n - k                            # 타입 별로 한 명씩 배치하고 남은 멘토들

    for start, ing, typ in reqs:
        table[typ].append((start, ing))

    # 남은 멘토를 어떻게 하면 재배치 할 지 고민 필
    search(table, rest, k)
    return answer
