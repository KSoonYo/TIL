# 문제

https://school.programmers.co.kr/learn/courses/30/lessons/12938

# 풀이

- n개의 각 원소의 합이 s가 되어야 하고, 각 원소의 곱이 최대가 되어야 함
- s를 n으로 나누면 -> n개의 수로 s를 이룰 수 있는 수 중 가장 큰 값의 경계(하한)를 구할 수 있음
- s를 n으로 나눈 몫을 s에서 빼고 남은 수 rest는 곧 n - 1개의 수들의 합으로 만들어야 하는 수
- 부분문제: rest에서 n - 1개로 나누면 n - 1개의 수로 rest를 이룰 수 있는 수 중 가장 큰 값의 경계를 구할 수 있음
- n = 1이면 나머지 값 그대로 조합에 추가된다.
- 만약 몫이 0이 나오면, 해당 수는 n개의 조합으로 만들 수 없는 수

```python

def solution(n, s):
    answer = []

    while n:
        mid = s // n
        if not mid:
            return [-1]
        s -= mid
        n -= 1
        answer.append(mid)

    return answer

```
