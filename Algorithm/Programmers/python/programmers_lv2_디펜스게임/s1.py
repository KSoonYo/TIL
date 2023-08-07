import heapq


def solution(n, k, enemy):
    '''
    현재 적의 수가 남은 병사의 수보다 크면, 이전 라운드에서 가장 많은 병사가 죽은 라운드의 병사를 k - 1 해서 소생
    --> 50% fail
    --> 수정) 일단 현재 막을 적의 수를 heapq에 넣어놓고, 남은 병사 수가 적보다 적고 k가 0보다 크면 무적권을 사용해서 병사 수를 보강한 후에 적을 방어 
    '''

    if k >= len(enemy):
        return len(enemy)

    q = []
    rnd = 0
    for amount in enemy:
        heapq.heappush(q, (-amount, amount))  # 최대 힙 유지
        if n < amount and k > 0:
            n += heapq.heappop(q)[1]          # 회복
            k -= 1
        elif n < amount:
            break
        n -= amount                           # 방어
        rnd += 1

    return rnd
