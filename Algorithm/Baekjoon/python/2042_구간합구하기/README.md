# 문제

어떤 N개의 수가 주어져 있다. 그런데 중간에 수의 변경이 빈번히 일어나고 그 중간에 어떤 부분의 합을 구하려 한다. 만약에 1,2,3,4,5 라는 수가 있고, 3번째 수를 6으로 바꾸고 2번째부터 5번째까지 합을 구하라고 한다면 17을 출력하면 되는 것이다. 그리고 그 상태에서 다섯 번째 수를 2로 바꾸고 3번째부터 5번째까지 합을 구하라고 한다면 12가 될 것이다.

## 입력

첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)과 M(1 ≤ M ≤ 10,000), K(1 ≤ K ≤ 10,000) 가 주어진다. M은 수의 변경이 일어나는 횟수이고, K는 구간의 합을 구하는 횟수이다. 그리고 둘째 줄부터 N+1번째 줄까지 N개의 수가 주어진다. 그리고 N+2번째 줄부터 N+M+K+1번째 줄까지 세 개의 정수 a, b, c가 주어지는데, a가 1인 경우 b(1 ≤ b ≤ N)번째 수를 c로 바꾸고 a가 2인 경우에는 b(1 ≤ b ≤ N)번째 수부터 c(b ≤ c ≤ N)번째 수까지의 합을 구하여 출력하면 된다.

입력으로 주어지는 모든 수는 -263보다 크거나 같고, 263-1보다 작거나 같은 정수이다.

## 출력

첫째 줄부터 K줄에 걸쳐 구한 구간의 합을 출력한다. 단, 정답은 -263보다 크거나 같고, 263-1보다 작거나 같은 정수이다.

## 예제 입력 1

```
5 2 2
1
2
3
4
5
1 3 6
2 2 5
1 5 2
2 3 5
```

## 예제 출력 1

```
17
12
```

# 문제풀이

- `prefix sum` 방식으로 풀이 할 경우, 배열의 특정 인덱스를 수정하고 구간합 전체를 다시 갱신할 때 O(N) 만큼의 시간복잡도가 추가로 걸리고, 갱신 횟수가 최대 10,000까지 가능하므로 최악의 경우 `1,000,000 * 10,000` 만큼의 시간이 소요된다.
- 이처럼 구간합 갱신이 빈번한 경우, 구간합을 갱신하는 과정이 O(logN) 시간복잡도인 `세그먼트 트리`를 사용하는 것이 효율적
- 또한 구간합을 초기화하는 데 O(N)인 `prefix sum` 방식에 비해 `세그먼트 트리`는 O(logN)의 시간 복잡도가 소요된다.
- 다만 트리 자료구조이므로 메모리가 더 필요하다.
- [참고](https://www.codingninjas.com/codestudio/library/segment-tree-428)

```python
import sys
input = sys.stdin.readline

# 세그먼트 트리 초기화
def init(start, end, index):
    mid = (start + end) // 2
    if start > end:
        return 0
    if start == end:
        tree[index] = arr[start]
        return tree[index]

    left = index * 2
    right = index * 2 + 1

    tree[index] = init(start, mid, left) + init(mid + 1, end, right)
    return tree[index]

# 구간합 구하는 로직
def get_sum(start, end, index, left, right):
    '''
    start: 트리의 현재 노드에서의 시작 구간
    end: 트리의 현재 노드에서의 끝 구간
    index: 트리의 현재 노드
    left: 구하고자 하는 구간의 시작
    right: 구하고자 하는 구간의 끝
    '''

    # 구하고자 하는 구간이 현재 트리의 구간을 벗어나는 경우를 제외
    if left > end or right < start:
        return 0

    # 노드의 구간이 구하고자 하는 범위에 속하는 경우에 대해 현재 노드의 값을 반환
    if left <= start and right >= end:
        return tree[index]

    mid = (start + end) // 2
    return get_sum(start, mid, index * 2, left, right) + get_sum(mid + 1, end, index * 2 + 1, left, right)

# 배열의 특정 인덱스의 값을 수정할 때 구간합 갱신 로직
def update(start, end, index, target, diff):
    '''
    start: 트리의 현재 노드에서의 시작 구간
    end: 트리의 현재 노드에서의 끝 구간
    index: 트리의 현재 노드
    target: 배열에서 수정하려는 값의 인덱스
    diff: 배열에서 수정하기 전의 값과 수정 후의 값의 차이
    '''

    if target < start or target > end:
        return

    tree[index] -= diff                     # 구간합 갱신

    if start == end:
        return

    mid = (start + end) // 2
    update(start, mid, index * 2, target, diff)
    update(mid + 1, end, index * 2 + 1, target, diff)
    return


N, M, K = map(int, input().split())

# segment tree
tree = [0] * (N * 4 + 1)                # 세그먼트 트리의 길이는 배열 길이 N
arr = [0] * (N + 1)
for i in range(1, N + 1):
    arr[i] = int(input())

init(1, N, 1)                           # segment 트리 초기화

for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        diff = arr[b] - c
        arr[b] = c
        update(1, N, 1, b, diff)
    if a == 2:
        print(get_sum(1, N, 1, b, c))

```
