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
    if left > end or right < start:
        return 0
    
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
tree = [0] * (N * 4 + 1)
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



