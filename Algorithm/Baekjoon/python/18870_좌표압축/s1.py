N = int(input())

# 숫자 정렬
numbers_origin = list(map(int, input().split()))
numbers = sorted(numbers_origin)

lower_bound = {
    'index': 0,
    'value': numbers[0],
    'end': numbers[-1],
}

# 가장 작은 인덱스부터 순차적으로 각각의 숫자가 몇번째로 큰 숫자인지 기록
# 단, 중복은 고려 x
# ex) -10, -9, 2, 4, 4 -> 0, 1, 2, 3, 3
table = {}
start = numbers[0]
table[start] = 0
for i in range(1, N):
    key = numbers[i]
    if key > lower_bound['value']:
        table[key] = lower_bound['index'] + 1
        lower_bound['index'] += 1
        lower_bound['value'] = key

result = []
for number in numbers_origin:
    result.append(table[number])

print(*result)