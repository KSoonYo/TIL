import sys
input = sys.stdin.readline

N = int(input())
stairs = [0] * (N + 1)
dp = [[0, 0] for _ in range(N + 1)]     # [i - 2 계단에서 현재 계단으로 오는 경우, i - 1 계단에서 현재 계단으로 오는 경우]
for i in range(1, N + 1):
    stairs[i] = int(input())

dp[1] = [stairs[1], stairs[1]]          # 1번째 계단 초기화
if N == 1:
    print(stairs[1])
    exit()

for i in range(2, N + 1):                                               # 한 계단 전에서 오려면 먼저 i - 1 계단까지 두 계단 점프를 해야 한다.(3계단 연속으로 밟을 수 없기 때문)
    dp[i] = [max(dp[i - 2]) + stairs[i], dp[i - 1][0] + stairs[i]]      # 두 계단 전에서 현재 계단까지 점프하는 경우, 두 계단 전에 도달하는 경우의 최대치에서 현재 계단 수를 더한다.
print(max(dp[N]))
