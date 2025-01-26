def convertToSeconds(t: str) -> int:
    parsed_hour, parsed_minute, parsed_second = t.split(':')
    hour = int(parsed_hour) * 3600
    minute = int(parsed_minute) * 60
    second = int(parsed_second)

    return hour + minute + second


def convertToString(t: int) -> str:

    hour, minute, second = t // 3600, t % 3600 // 60, t % 3600 % 60

    return f'{hour if hour >= 10 else "0" + str(hour)}:{minute if minute >= 10 else "0" + str(minute)}:{second if second >= 10 else "0" + str(second)}'


def solution(play_time, adv_time, logs):
    # 특정 초에 시청되고 있는 레코드의 변화량 기록 테이블
    events = [0] * (convertToSeconds(play_time) + 1)

    for log in logs:
        start, end = log.split('-')
        events[convertToSeconds(start)] += 1
        events[convertToSeconds(end)] -= 1

    prefix_sum = [0] * (convertToSeconds(play_time) +
                        1)    # 특정 초에 걸쳐 있는 레코드의 개수 누적합 기록 테이블

    prefix_sum[0] += events[0]

    for i in range(convertToSeconds(play_time)):
        prefix_sum[i + 1] = prefix_sum[i] + events[i + 1]

    converted_adv = convertToSeconds(adv_time)

    window = [0, 0]           # (시작점, 누적 재생 레코드 수)

    # 시작 지점(00:00:00) 부터 광고 시간까지의 레코드 누적 합 계산
    for i in range(converted_adv + 1):
        window[1] += prefix_sum[i]

    maxV = window[1]
    for i in range(converted_adv, len(prefix_sum)):
        # 윈도우 이동
        window[1] -= prefix_sum[i - converted_adv]
        window[1] += prefix_sum[i]

        if window[1] > maxV:
            maxV = window[1]
            window[0] = i - converted_adv + 1

    return convertToString(window[0])


answer = solution("99:59:59", "25:00:00", [
    "69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"])
answer = solution("50:00:00", "50:00:00", [
    "15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"])
print(answer)
