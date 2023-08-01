# 문제

https://school.programmers.co.kr/learn/courses/30/lessons/142085

# 풀이

- 처음 풀이) 현재 적의 수가 남은 병사의 수보다 크면 이전 라운드에서 가장 많은 병사가 죽은 라운드의 병사를 k-1해서 소생

  - 라운드를 시작하자마자 곧바로 무적권을 사용하는 상황에 대한 케이스가 고려되지 않음
  - ex) 첫번째 라운드부터 무적권을 사용하는 상황이면 '이전 라운드에서 가장 많은 병사가 죽은 라운드의 병사'를 부활시킬 수 없음

- 수정한 풀이) 일단 현재 라운드에서 방어에 필요한 병사 수를 heapq에 넣어 최대힙을 유지하고, 현재 라운드에서 남은 병사 수가 적보다 적고 k가 0보다 크면 무적권을 사용해서 heapq에서 최대로 보강할 수 있는 병사 수를 꺼내 더하여 적군을 막아내는 방법

```python
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

```
