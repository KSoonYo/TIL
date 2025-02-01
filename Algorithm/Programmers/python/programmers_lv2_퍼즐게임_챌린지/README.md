# 문제

https://school.programmers.co.kr/learn/courses/30/lessons/340212?language=python3

# 풀이

## 접근 방법

1. 이 문제는 이진 탐색을 통해 최적의 숙련도(level)를 찾는 문제이다.

2. 주어진 제한시간(limit) 내에서 모든 퍼즐을 해결할 수 있는 최소 숙련도를 찾아야 한다.

3. 각 퍼즐을 해결하는데 필요한 시간은 다음과 같이 계산된다:
   - 퍼즐의 난이도(diff)가 숙련도(level)보다 작거나 같은 경우: solve_time
   - 퍼즐의 난이도가 숙련도보다 큰 경우: (diff - level) \* (solve_time + back_time) + solve_time

## 구현 방법

1. 이진 탐색의 범위:

   - left = 1 (최소 숙련도)
   - right = max(diffs) (최대 난이도)

2. 중간값(level)을 기준으로 모든 퍼즐을 해결하는데 걸리는 총 시간을 계산한다.

3. 총 시간이 제한시간을 초과하는 경우:

   - 숙련도를 높여야 하므로 left = mid + 1로 설정한다.

4. 총 시간이 제한시간 이하인 경우:
   - 현재 숙련도를 정답 후보로 저장한다.
   - 더 작은 숙련도로도 가능한지 확인하기 위해 right = mid - 1로 설정한다.

## 시간 복잡도

- 이진 탐색: O(log M) (M은 최대 난이도)
- 각 단계에서 모든 퍼즐 확인: O(N)
- 전체 시간 복잡도: O(N \* log M)이다.

## 공간 복잡도

- O(1)의 추가 공간만 사용한다.

---

## 코드

```python
def calculate(diff, solve_time, back_time, level):
    result = 0
    if (diff <= level):
        result += solve_time
    else:
        solve_cnt = diff - level
        cost_time = solve_cnt * (solve_time + back_time) + solve_time
        result += cost_time

    return result


def solution(diffs, times, limit):
    answer = 10**15

    n = len(diffs)
    maxV = max(diffs)

    left = 1
    right = maxV

    while (left <= right):
        level = (left + right) // 2

        total = 0
        over = False
        for i in range(n):
            diff = diffs[i]
            t = times[i]
            total += calculate(diff, t, 0 if i == 0 else times[i - 1], level)

            if total > limit:
                over = True
                break
        if over:
            left = level + 1
        else:
            answer = min(level, answer)
            right = level - 1

    return answer

```
