# 문제
https://www.acmicpc.net/problem/1654

# 풀이
- 간단한 이분탐색 문제
- 현재 주어진 랜선의 길이 중 가장 긴 것을 구하고, 시작점 1부터 끝점 max_length의 mid(중간값)를 구한다.
  - 중간값으로 랜선을 다 잘라보면서 N 이상의 개수가 나오는지 체크
  - N 이상의 개수가 나오면 최대값을 갱신하고 시작점을 mid + 1로 늘린다.
  - N보다 적게 나누어지면 right을 mid - 1로 줄여서 범위를 좁힌다. 
```python
import sys
input = sys.stdin.readline


K, N = map(int, input().split())
lines = []
for _ in range(K):
    lines.append(int(input()))

l, r = 1, max(lines)
answer = 0
while l <= r:
    mid = (l + r) // 2
    temp = 0
    for line in lines:
        temp += (line // mid)
    
    if temp >= N:
        l = mid + 1
        answer = max(answer, mid)
    else:
        r = mid - 1
print(answer)

```
