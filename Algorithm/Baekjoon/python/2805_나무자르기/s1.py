

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
