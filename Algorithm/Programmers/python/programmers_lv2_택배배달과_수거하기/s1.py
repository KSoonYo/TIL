# fail
def solution(cap, n, deliveries, pickups):
    answer = 0
    # 가장 멀리 있는 배달 포인트부터 수량 계산 -> cap 이하 범위까지 집에 배달
    # 배달 후에 가장 멀리 있는 곳부터 수거 -> cap 이하 범위까지 수거
    d_target = n - 1
    houses = 0
    d_temp = 0
    
    while d_target >= 0:
        if d_temp + deliveries[d_target] > cap or d_target == 0:
            answer += (d_target + houses + 1) * 2        # 왕복 2회 거리 계산
            p_target = d_target + houses
            p_cap = cap
            while p_cap > 0 and p_target >= 0:           # 배달 완료 후 수거
                if pickups[p_target] >= p_cap:
                    pickups[p_target] -= p_cap
                    break
                p_cap -= pickups[p_target]
                pickups[p_target] = 0
                p_target -= 1
            
            if d_target == 0:
                break
            
            d_temp = 0
            houses = 0
            continue
        d_temp += deliveries[d_target]                  
        d_target -= 1
        houses += 1
    
    return answer

# 2차 풀이
# 참고: https://school.programmers.co.kr/questions/43364
def solution(cap, n, deliveries, pickups):
    answer = 0
    d, p = 0, 0
    for i in range(n - 1, -1, -1):
        cnt = 0                             # 운반 횟수
        d -= deliveries[i]                  # 배송량 저장
        p -= pickups[i]                     # 수거량 저장
        while d < 0 or p < 0:               # 배송량 혹은 수거량을 충족할 때까지 i 집으로 가야하는 횟수 구하기
            d += cap                        # 남는 양은 i까지 오는 과정에서 방문한 이전 집에서 그대로 사용 가능
            p += cap                        # 핵심은 배송량과 수거량을 0 이상 유지시키는 것
            cnt += 1
        answer += (i + 1) * 2 * cnt
    return answer


print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))


