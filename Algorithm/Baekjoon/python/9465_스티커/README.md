# 문제

https://www.acmicpc.net/problem/9465

# 풀이

- 2차원 dp 문제
- 아래 스티커라면 -> 이전 스티커 중 대각선 위 방향에 있는 스티커, 대각선 위 방향의 스티커의 이전 스티커 중 최대값을 현재 스티커 위치에 더함
- 위 스티커라면 -> 이전까지의 스티커 중 대각선 아래 방향에 있는 스티커, 대각선 아래 방향의 스티커의 이전 스티커 중 최대값을 현재 스티커 위치에 더함
- 주의) num이 1인 경우에 대한 예외처리 필요

```python
case = int(input())
case_num = 0
final_result = []

while case_num < case:
    num = int(input())
    num_list = [[0 for i in range(num)] for j in range(2)]
    num_list[0] = list(map(int, input().split()))
    num_list[1] = list(map(int, input().split()))

    if num > 1:
        num_list[0][1] += num_list[1][0]
        num_list[1][1] += num_list[0][0]

    for h in range(2, num):
        num_list[0][h] += max(num_list[1][h-1], num_list[1][h-2])
        num_list[1][h] += max(num_list[0][h-1], num_list[0][h-2])
    final_result.append(max(num_list[0][num-1], num_list[1][num-1]))
    case_num += 1

for k in range(len(final_result)):
    print(final_result[k])
```
