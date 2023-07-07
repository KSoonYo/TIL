# 풀이1) 정렬을 이용한 풀이 -> 빨리 퇴실하는 방부터 비우고 새로 채우는 방식
def clean(time):
    h, m = map(int, time.split(':'))
    after_cleaning = m + 10
    h += (after_cleaning // 60)
    m = after_cleaning % 60
    str_m = str(m)
    if m > 0:
        if m < 10:
            str_m = '0' + str_m
    else:
        str_m = '00'
    to_str = f'{h if h > 9 else "0" + str(h)}:{str_m}'
    return to_str



def solution(book_time):
    sorted_time = sorted(book_time, key=lambda x : x[0])
    rooms = []
    for start, end in sorted_time:
        if not rooms:
            rooms.append([start, end])
            continue
        rooms.sort(key=lambda x : x[1], reverse=True)
        if start < clean(rooms[-1][1]):
            rooms.append([start, end])
        else:
            rooms.pop()
            rooms.append([start, end])
    return len(rooms)


# 풀이2) 누적합을 이용한 풀이 -> 분 단위로 각 시간대에 예약 인원을 체크하는 방식 
def time2min(time):
    hour = int(time[:2])
    minute = int(time[3:])
    return hour * 60 + minute

def solution(book_time):
    answer = 0
    minute = [0 for _ in range(24*60 + 10)]

    for book in book_time:
        start = time2min(book[0])
        end = time2min(book[1])
        minute[start] += 1
        minute[end+10] += -1
    num = 0
    for i in range(len(minute)):
        num += minute[i]
        minute[i] = num

    answer = max(minute)

    return answer