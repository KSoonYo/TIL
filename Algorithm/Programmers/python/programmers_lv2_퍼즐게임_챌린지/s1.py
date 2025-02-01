def calculate(diff, solve_time, back_time, level):
    result = 0
    if (diff <= level):
        result += solve_time
    else:
        solve_cnt = diff - level
        cost_time = solve_cnt * (solve_time + back_time) + solve_time
        result += cost_time

    return result


def solution(diffs, times, limit):
    answer = 10**15

    n = len(diffs)
    maxV = max(diffs)

    left = 1
    right = maxV

    while (left <= right):
        level = (left + right) // 2

        total = 0
        over = False
        for i in range(n):
            diff = diffs[i]
            t = times[i]
            total += calculate(diff, t, 0 if i == 0 else times[i - 1], level)

            if total > limit:
                over = True
                break
        if over:
            left = level + 1
        else:
            answer = min(level, answer)
            right = level - 1

    return answer
