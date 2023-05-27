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
