from collections import deque

for _ in range(int(input())):
  N = int(input())
  strings = input().split()

  # 최대한 사전 순으로 빠른 문자를 앞에 배치 시킨다.  
  start_char = strings[0]
  front = start_char
  result = deque([start_char])

  for i in range(1, N):
    if front >= strings[i]:
      front = strings[i]
      result.appendleft(strings[i])
      continue
    
    result.append(strings[i])
  
  result = ''.join(list(result))
  print(result)