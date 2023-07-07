# 문제

https://school.programmers.co.kr/learn/courses/30/lessons/155651

# 풀이

## 나의 풀이(그리디)

1. 우선 시작 시간을 기준으로 정렬
2. 정렬된 시간을 순회해서 예약을 받음
   1. 이전에 예약 받은 방들을 매번 정렬
   2. 가장 빨리 퇴실하는 방의 퇴실시간보다 현재 예약 체크인 시간이 크다면 방을 추가
   3. 퇴실 시간 이후라면 방을 하나 비우고 새로 방을 추가

- 문제점) 그리디 방식이기 때문에 최적해를 보장할 순 없음(예외 케이스에 주의를 기울여야 함)
- 주의)
  - 문자열 형식으로 시간을 비교할 때, 예를 들어 '06'이 '6'보다 작게 나올 수 있음에 주의

```python
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
```

## 다른 풀이(누적합)

1. 최대 시간이 23:59 이므로 분으로 환산하여 최대 길이의 시간 배열 생성
2. 모든 예약 시간을 분으로 환산
3. 예약 리스트를 순회하면서 입실 시간에 +1, 퇴실 시간에 -1
4. 시간 배열을 순회 -> 해당 시간까지 사용된 방의 개수를 누적해가며 배열 요소 갱신

```python
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
```
