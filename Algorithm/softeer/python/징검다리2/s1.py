# 6개 정답...
# 반례)
# 10
# 1 200 3 4 2 10 8 5 8 2
# 정답: 7
#####
# 이 풀이의 문제점
# 1) 첫번째 돌부터 반드시 시작해야 한다는 전제가 없으므로 최대 길이를 보장할 수 없음
# 2 - 1) 위 반례에서 1, 3, 4 까지 3개의 돌을 밟고, 2를 밟지 않고 10을 밟으면 4개의 돌을 밟을 수 있음
# 2 - 2) 하지만 이 풀이에서는 1 3 4 까지 3개의 돌만 기억하고 높이가 낮은 돌이 나오는 순간 1 2 로 stack이 갱신되어 10을 밟으면 3개의 돌을 밟는 것으로 계산된다.
# 2 - 3) 따라서 stack으로 증가 수열의 길이를 계산하는 것은 일부 케이스에서는 틀릴 수 있음
# 3) stack으로 풀어야 하는 문제의 대표 예시: https://school.programmers.co.kr/learn/courses/30/lessons/154539

N = int(input())
stones = list(map(int, input().split()))
counts1 = [0] * N
counts2 = [0] * N

stack = []
cnt = 0
for i in range(N):
    height = stones[i]

    while stack and stack[-1] >= height:
        stack.pop()
        cnt -= 1
    stack.append(height)
    cnt += 1
    counts1[i] = cnt

stack2 = []
cnt2 = 0
for j in range(N - 1, -1, -1):
    height = stones[j]

    while stack2 and stack2[-1] >= height:
        stack2.pop()
        cnt2 -= 1
    stack2.append(height)
    cnt2 += 1
    counts2[j] = cnt2

maxV = 0
for k in range(N):
    result = counts1[k] + counts2[k] - 1
    maxV = max(maxV, result)

print(counts1)
print(counts2)
print(maxV)
