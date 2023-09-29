from itertools import combinations

N = int(input())
snows = list(map(int, input().split()))
candidates_origin = []

for i in range(N):
    candidates_origin.append((i, snows[i]))

# 2개의 눈뭉치로 만들 수 있는 눈사람 집합(눈덩이 2개의 조합)
candidates = list(combinations(candidates_origin, 2))

# 눈사람의 키 오름차순으로 정렬
candidates.sort(key=lambda x: x[0][1] + x[1][1])

length = len(candidates)
minV = 1000000001
for k in range(length):
    a1, a2 = candidates[k]
    idx1, idx2 = a1[0], a2[0]
    value1 = a1[1] + a2[1]
    # value1과 value2는 각각 안나와 엘사(혹은 엘사와 안나)가 선택한 눈사람
    for h in range(k + 1, length):
        b1, b2 = candidates[h]
        idx3, idx4 = b1[0], b2[0]

        # 다른 사람이 이미 고른 눈덩이는 제외
        if idx1 == idx3 or idx1 == idx4 or idx2 == idx3 or idx2 == idx4:
            continue
        value2 = b1[1] + b2[1]
        minV = min(minV, abs(value2 - value1))

        # 눈사람 키 순으로 오름차순 정렬을 한 상태이기 때문에 이후의 눈사람을 고르면 차이가 더 커지기만 한다.
        # 최소의 차를 구하는 것이므로 최소값 갱신 이후 break
        break
print(minV)
