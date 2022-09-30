
# 첫번째부터 다섯번째 장소 중 두 번째 또는 세번째 장소를 방문하는 모든 경우를 찾을 때
for i in range(1 << 5):
    if i & 1 << 1 or i & 1 << 2:
        print(format(i, 'b'))


# 주어진 상태에서 두번째나 세번째 장소를 방문했는지 여부를 체크하는 경우
status = (1 << 0) + (1 << 2) + (1 << 3) + (1 << 4)
print('status: ', format(status, 'b'))
if status & 1 << 1 or status & 1 << 2:
    print('true')
else:
    print('false')


# 특정 장소에 다다랐을 때 방문체크하는 경우
# 원래 상태에서 네번째 장소를 방문했을 때를 체크해야 한다면
origin = 0b00100
print(format(origin | 1 << 3, 'b'))