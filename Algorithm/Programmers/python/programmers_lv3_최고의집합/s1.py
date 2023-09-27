
def solution(n, s):
    answer = []

    # n개의 숫자 총합으로 s가 될 수 있는 수 중 가장 큰 수의 경계 -> s // n
    # 부분문제: s에서 이전의 큰 수를 빼고 남은 수 -> n - 1개의 숫자 총합으로 만들어야 하는 수
    while n:
        mid = s // n

        # mid가 0이 되면 n개의 조합으로 만들 수 없는 수
        if not mid:
            return [-1]
        s -= mid
        n -= 1
        answer.append(mid)

    return answer
