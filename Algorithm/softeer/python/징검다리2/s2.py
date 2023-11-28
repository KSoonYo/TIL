
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
