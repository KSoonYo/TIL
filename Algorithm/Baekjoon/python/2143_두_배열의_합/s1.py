'''
부배열 합을 구하는 부분을 너무 어렵게 생각한 듯

입력값 최대 길이가 1000 이고 시간 제한이 2초이므로 이중 for문으로 누적합을 저장해도 된다.
핵심은 
1. 이분 탐색이나 투 포인터로 부분쌍의 개수 찾기
2. 찾고자 하는 target이 여러 개인 경우에 대한 처리(중복 원소 개수 카운트)

'''


def search(target):
    global bn, b_table, hash_table

    result = 0
    left = 0
    right = len(b_table) - 1

    while left <= right:
        mid = (left + right) // 2

        if b_table[mid] > target:
            right = mid - 1
        if b_table[mid] == target:
            result += hash_table[target]
            break
        if b_table[mid] < target:
            left = mid + 1

    return result


T = int(input())
an = int(input())
a_list = list(map(int, input().split()))

bn = int(input())
b_list = list(map(int, input().split()))

answer = 0


a_dp = [[None] * (an + 1) for _ in range(an)]  # a의 부배열 합에 대한 메모 테이블
b_dp = [[None] * (bn + 1) for _ in range(bn)]  # b의 부배열 합에 대한 메모 테이블


a_table = []
b_table = []

hash_table = {}

# 초기화
for k in range(1, max(an, bn) + 1):
    if an >= k:
        a_dp[k - 1][1] = a_list[k - 1]
        a_table.append(a_dp[k - 1][1])
    if bn >= k:
        b_dp[k - 1][1] = b_list[k - 1]
        b_table.append(b_dp[k - 1][1])
        hash_table[b_dp[k - 1][1]] = hash_table.get(b_dp[k - 1][1], 0) + 1


# 원소 개수 별 dp 실행
# j = 1면 하나, j = 2이면 둘 ...
# j는 원소의 개수를 의미, k는 j 원소 조합 각각의 순서
# 원소 하나에 대해서는 초기화를 했으므로 둘부터 시작

for j in range(2, max(an, bn) + 1):
    for k in range(max(an, bn) - j + 1):
        if an >= j and an >= k and k + j - 1 < an:
            # dp[k][j]는 j - 1(이전 자릿수의 조합)에서 바로 다음 순서에 있는 원소 하나를 더한 것
            a_dp[k][j] = a_dp[k][j - 1] + a_dp[k + j - 1][1]
            a_table.append(a_dp[k][j])
        if bn >= j and bn >= k and k + j - 1 < bn:
            b_dp[k][j] = b_dp[k][j - 1] + b_dp[k + j - 1][1]
            b_table.append(b_dp[k][j])
            hash_table[b_dp[k][j]] = hash_table.get(b_dp[k][j], 0) + 1

# 이분탐색을 위한 정렬
b_table.sort()

for elem in a_table:
    # T에서 a 원소 값만큼 제외한 것이 b_table에 몇 개 있는지에 따라 부배열 쌍 개수가 결정된다.
    answer += search(T - elem)
print(answer)
