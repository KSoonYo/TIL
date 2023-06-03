import math

def solution(r1, r2):
    # 원의 방정식
    # (x-a)^2 + (x-b)^2 = r^2
    # 원 내부의 점 조건 -> (x - a)^2 + (x - b)^2 < r^2
    # 사분면 하나에 대한 점 개수를 구하고 * 4(이때 x = 0일때를 제외해서 겹치는 부분 제거)
    # 주의) 올림처리를 math.floor() 혹은 int()로 하고 +1을 해서 처리하면, 
    # 5^2 - 3^2 = 4^2 경우에 대해서 y = 4가 되어야 함에도 y = 5가 되어 버린다.(원 위에 있는 점은 빼면 안된다!)
    cnt = 0
    for x in range(1, r2 + 1):
        y1 = 0
        if x < r1:
            y1 = math.ceil((r1 ** 2 - x ** 2) ** 0.5)
        y2 = math.floor((r2 ** 2 - x ** 2) ** 0.5)
        cnt += (y2 - y1 + 1)
    return cnt * 4