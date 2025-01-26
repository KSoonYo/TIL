
people, cnt = map(int, input().split())

snacks = list(map(int, input().split()))
snacks.sort()

left = 1
right = max(snacks)
maxV = float('INF')

while left <= right:
    mid = (left + right) // 2   # 막대 과자 길이

    given = 0
    is_ok = False
    for snack in snacks:
        if snack >= mid:
            # snack을 mid로 나눈 몫만큼 조카에게 과자를 나눠주고, 막대 과자 길이를 쪼개고 남은 과자 길이에 대해 다시 나눠준다.
            given += (snack // mid + (snack % mid) // mid)

        if given >= people:
            is_ok = True
            break

    if is_ok:
        maxV = mid
        left = mid + 1          # 모든 조카들에게 막대 과자를 나눠줬다면 길이를 늘려본다.
    else:
        right = mid - 1         # 모든 조카들에게 막대 과자를 나눠주지 못했다면 길이를 좁혀본다.

print(maxV if maxV != float('INF') else 0)
