# 문제
https://www.acmicpc.net/problem/2447

# 풀이
- 재귀를 이용한 간단한 분할 정복 문제
- N이 3일때의 패턴이 기본 패턴
  - N이 3보다 큰 경우 (N // 3)을 하면서 N = 3일 때 기본 패턴을 먼저 완성 시키고(top-down), 그 다음 N = 9, 27 ...로 올라가면서 이전에 그렸던 패턴을 반복적으로 그린다.(bottom-up)
  - N이 3의 거듭제곱이므로 공백으로 비워야 하는 가운데의 시작점은 (시작점_r + N // 3, 시작점_c + N // 3)이다. (가장 첫 시작점을 0,0 이라고 할 경우)
  
```python

def stars(s, paper, k):
    r, c = s
    jump = k // 3 

    if k == 3:
        for i in range(r, r + 3):
            for j in range(c, c + 3):
                if i == r + jump and j == c + jump:
                    continue
                paper[i][j] = '*'
        return

    for i in range(r, r + k, jump):
        for j in range(c, c + k, jump):
            if r + jump <= i < r + jump * 2 and c + jump <= j < c + jump * 2:
                continue
            stars((i, j), paper, jump)
    return



N = int(input())
paper = [[' '] * N for _ in range(N)]
stars((0, 0), paper, N)
for i in range(N):
    for j in range(N):
        print(paper[i][j], end='')
    print()
```
