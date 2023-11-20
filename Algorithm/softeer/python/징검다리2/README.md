# 문제

https://softeer.ai/practice/6290

# 풀이

- 배열 왼쪽애서 오른쪽, 오른쪽에서 왼쪽으로 양방향 순회를 해서 올라갔다가 내려가는 경우를 계산하는 문제
- 돌의 높이(height)를 순회
  - 만약 현재 돌의 높이가 배열의 가장 큰 높이보다 작거나 같다면
    - 이분 탐색(binary search)으로 배열 arr에서 현재 높이보다 낮거나 같은 돌 중 가장 큰 돌의 위치(lower bound)를 구한다.
    - count 배열로 현재 돌의 인덱스에 lower bound의 위치에서 +1한 값을 기록한다.(lower bound까지 돌을 밟고 현재 돌을 밟으므로)
    - arr 배열에서 lower bound 돌 위치의 값을 현재 돌의 높이로 갱신한다.
  - 현재 돌의 높이가 배열의 가장 큰 높이보다 크다면
    - 배열에 해당 돌의 높이를 추가하고 count 배열에 추가한 만큼의 돌의 개수를 기록한다.
- 문제에서 돌을 오름차순으로 밟는다고 전제했기 때문에 돌을 밟는 높이는 기본적으로 오름차순 정렬이 전제된다.
  - **내려가는 길은 내려가는 방향의 반대 방향으로 올라가는 길이라는 점에 유의**

```python

def binary_search(arr, value):
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] < value:
            l = mid + 1
        elif arr[mid] == value:
            break
        else:
            r = mid - 1
    return l


N = int(input())
stones = list(map(int, input().split()))
counts1 = [0] * N
counts2 = [0] * N

arr = []
for i in range(N):
    height = stones[i]
    if arr and arr[-1] >= height:
        lower_bound = binary_search(arr, height)
        counts1[i] = lower_bound + 1
        arr[lower_bound] = height
        continue
    arr.append(height)
    counts1[i] = len(arr)

arr = []
for j in range(N - 1, -1, -1):
    height = stones[j]
    if arr and arr[-1] >= height:
        lower_bound = binary_search(arr, height)
        counts2[j] = lower_bound + 1
        arr[lower_bound] = height
        continue
    arr.append(height)
    counts2[j] = len(arr)

maxV = 0
for k in range(N):
    maxV = max(maxV, counts1[k] + counts2[k] - 1)
print(maxV)

```
