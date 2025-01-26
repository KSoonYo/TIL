
def get_lower_bound(s, target):
    global arr, N
    left = s
    right = N - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1

    return left


def get_upper_bound(s, target):
    global arr, N
    left = s
    right = N - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid - 1
        elif arr[mid] == target:
            left = mid + 1
        else:
            left = mid + 1

    return left


N = int(input())
arr = list(map(int, input().split()))
arr.sort()  # 오름차순 정렬
answer = 0

for i in range(N):
    for j in range(i + 1, N):
        n1, n2 = arr[i], arr[j]
        target = 0 - (n1 + n2)
        lower_bound = get_lower_bound(j + 1, target)
        upper_bound = get_upper_bound(j + 1, target)
        if lower_bound < N and arr[lower_bound] == target:
            answer += (upper_bound - lower_bound)

print(answer)

'''
bset solution
https://2hs-rti.tistory.com/entry/%EB%B0%B1%EC%A4%80-3151%EB%B2%88-%ED%95%A9%EC%9D%B4-0-%ED%8C%8C%EC%9D%B4%EC%8D%AC


from bisect import bisect_left

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

answer = 0
for i in range(len(arr)-2):
    left, right = i+1, N-1
    while left < right:
        result = arr[i]+arr[left]+arr[right]
        if result > 0:
            right -= 1
        else:
            if result == 0:
                if arr[left] == arr[right]:
                    answer += right - left
                else:
                    idx = bisect_left(arr, arr[right])
                    answer += right-idx+1
            left += 1

print(answer)

'''
