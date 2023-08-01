# 문제

https://www.acmicpc.net/problem/2805

# 풀이

- 전형적인 이분탐색 문제
- 1부터 현재 나무 길이 중 가장 긴 나무길이 중 이분탐색으로 적정 나무길이를 구함
  - 현재의 mid 나무 길이로 나무를 잘라보면서 M 미터 이상 나무를 챙길 수 있으면 오른쪽으로 범위를 좁히고(최대 높이를 구해야 하므로 최대 높이값도 갱신), M 미터도 안되면 현재 높이가 너무 크다는 것이므로 왼쪽으로 범위를 좁혀서 이분탐색을 해본다.

```python

N, M = map(int, input().split())
trees = list(map(int, input().split()))
left = 1
right = max(trees)
answer = 0
while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for tree in trees:
        if tree > mid:
            cnt += (tree - mid)
        if cnt >= M:
            break
    if cnt >= M:
        left = mid + 1
        answer = max(answer, mid)
    else:
        right = mid - 1

print(answer)

```
