import heapq

# 카드 두 묶음을 합치면서 최소 비용을 보장하는 방법
# 최소 비용으로 두 카드를 합치고, 우선순위 큐에 합치기
# 이때 총 비용을 구하려면 비용을 합칠 때마다 누적
# 참고) 허프만 코딩

N = int(input())
last_amount = 0
costs = 0
arr = []

for _ in range(N):
    heapq.heappush(arr, int(input()))

if len(arr) == 1:
    print(0)
    exit()

while len(arr) > 1:
    node1 = heapq.heappop(arr)
    node2 = heapq.heappop(arr)

    costs += (node1 + node2)
    heapq.heappush(arr, node1 + node2)


print(costs)
