def calc(s, target, bits):
    '''
    1 ~ target 까지 1의 총합
    s: 타겟이 포함되는 구간인 n 단계
    target: 끝 범위
    bits: n 단계 별 최대 비트 개수
    '''
    base = [1, 1, 2, 2, 3, 4]
    result = 0
    # 과정 1 : 5 ** s-1로 target을 나눈 몫만큼 4 ** (s - 1) 을 result에 더한다.
    # 과정 2 : 1의 연산 과정에서 도출된 나머지를 새로운 target으로 갱신하고, 새로운 s를 search 하여 갱신한다. 단, 나머지가 0이면 그대로 종료한다. 1 <= 나머지 <= 5 라면 base[:나머지] 를 result에 더해주고 종료한다.
    
    # 추가 과정 1 : 만약 과정 1의 몫이 2이고 나머지가 1 이상이거나 몫이 3이고 나머지가 0이면 4 ** (s - 1) * 2를 result에 더하고 종료한다.
    # 추가 과정 2 : 만약 과정 1의 몫이 3 이상이고 나머지가 1 이상거나 몫이 4 이상이라면 4 ** (s - 1) * (몫 - 1) 만큼 result에 더해주고 과정 2로 넘어간다.
    if target == 0:                 # 타겟이 0이면 결과에 더해줄 것도 없으므로 return 0
        return 0
    while s >= 1:            
        # 과정 1
        volume = 5 ** (s - 1)
        quot = target // volume
        remained = target % volume
        ## 추가 과정 1
        if (quot == 2 and remained >= 1) or (quot == 3 and remained == 0):
            result += ((4 ** (s - 1)) * 2)
            break
        ## 추가 과정 2
        if (quot >= 3 and remained >= 1) or quot >= 4:
            result += (4 ** (s - 1) * (quot - 1))
        else:
            result += ((4 ** (s - 1)) * quot)
        
        # 과정 2
        if remained == 0:
            break
        if 1 <= remained <= 5:
            result += base[remained]
            break
        target = remained
        s -= 1   
    else:                     # s가 0인 경우
        return 1              # (조건에 따라) target이 가리키는 곳의 값은 무조건 1
    return result

def search(target, bits):
    for i in range(len(bits)):
        if target <= bits[i]:
            break
    return i

def solution(n, l, r):
    answer = 0
    bits = [5 ** i for i in range(n + 1)]       # n 당 최대 비트 개수
    
    l_s = search(l - 1, bits)
    r_s = search(r, bits)
        
    # l_s와 r_s를 구하고 1부터 r에서 1부터 l - 1까지의 합을 뺀다.
    l_result = calc(l_s, l - 1, bits)
    r_result = calc(r_s, r, bits)
    answer = r_result - l_result
    return answer