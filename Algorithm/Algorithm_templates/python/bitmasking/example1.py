# bitmasking example

# 숫자 집합
numbers = [1, 2, 3, 4]


for i in range(1 << len(numbers)):
    for j in range(len(numbers)):
        # 1을 << 연산을 하여 i의 각 자리에 있는 수와 & 연산
        # j만큼 왼쪽으로 1을 밀었을 때 i의 해당 자리 비트가 1이라면 숫자 집합에서 그 자리에 해당하는 인덱스를 출력
        if i & (1 << j):
            print(numbers[j], end = ' ')
    print()
    