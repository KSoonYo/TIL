

N, M, K = map(int, input().split())

beers = []
minLevel = 2 ** 31
maxLevel = 1

for _ in range(K):
    v, c = map(int, input().split())  # (선호도, 도수 레벨)
    beers.append((v, c))

    minLevel = min(minLevel, c)
    maxLevel = max(maxLevel, c)
    v, c = map(int, input().split())  # (선호도, 도수 레벨)
    beers.append((v, c))

    minLevel = min(minLevel, c)
    maxLevel = max(maxLevel, c)


left = minLevel
right = maxLevel

answer = -1

# 선호도 순으로 내림차순
beers.sort(key=lambda x: x[0], reverse=True)
while left <= right:
    cnt = 0
    temp = 0
    mid = (left + right) // 2

    for v1, c1 in beers:
        if c1 > mid:
            # 맥주 도수 레벨이 현재 레벨보다 높으면 skip
            continue

        temp += v1
        cnt += 1

        # 마셔야 하는 맥주 잔이 충족되었으먼 break
        if cnt == N:
            break

    # 마셔야 하는 맥주잔을 충족하지 못했다면, 레벨을 올려본다.
    if cnt < N:
        left = mid + 1
        continue

    # 채워야 하는 선호도 이상을 채웠다면 레벨을 낮춰본다.
    if temp >= M:
        right = mid - 1
        answer = mid
    else:
        # 아니라면 레벨을 올려본다.
        left = mid + 1


print(answer)


beers.sort(key=lambda x: x[0], reverse=True)
while left <= right:
    cnt = 0
    temp = 0
    mid = (left + right) // 2

    for v1, c1 in beers:
        if c1 > mid:
            # 맥주 도수 레벨이 현재 레벨보다 높으면 skip
            continue

        temp += v1
        cnt += 1

        # 마셔야 하는 맥주 잔이 충족되었으먼 break
        if cnt == N:
            break

    # 마셔야 하는 맥주잔을 충족하지 못했다면, 레벨을 올려본다.
    if cnt < N:
        left = mid + 1
        continue

    # 채워야 하는 선호도 이상을 채웠다면 레벨을 낮춰본다.
    if temp >= M:
        right = mid - 1
        answer = mid
    else:
        # 아니라면 레벨을 올려본다.
        left = mid + 1


print(answer)
