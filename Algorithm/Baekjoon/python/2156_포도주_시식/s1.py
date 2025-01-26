import sys
input = sys.stdin.readline


n = int(input())
wines = []
for _ in range(n):
  wines.append(int(input()))
 
if n < 3:
  print(sum(wines))
  exit()

# 3개 연속으로 마실 수 없음
# [2번째 전에만 마신 와인, 1번째 전에만 마신 와인, 2번째 및 1번째 전 모두 마신 와인] 이라고 할 때, 
# 2번째 및 1번째 전 모두 마신 와인에는 현재 와인 양을 더할 수 없음
# 또한 포도주가 다음 순서로 이동할 때마다 [2번째 전에만 마신 와인, 1번째 전에만 마신 와인, 2번째 및 1번째 전 모두 마신 와인]의 순서 또한 한 칸씩 로테이션 된다.
# 단, 논리적으로만 순서가 로테이션 될 뿐 원소 값의 순서 자체는 그대로
# [2번째 전에만 마신 와인, 1번째 전에만 마신 와인, 2번째 및 1번째 전 모두 마신 와인] -> [1번째 전에만 마신 와인, 2번째 및 1번째 전 모두 마신 와인, 2번째 전에만 마신 와인] ...

window = [] # [2번째 전에만 마신 와인, 1번째 전에만 마신 와인, 2번째 및 1번째 전 모두 마신 와인]
maxV = 0 # 마실 수 있는 최대 와인 양
guard = 2 # 더 마실 수 없는 가드 라인

for target_index in range(n):
  wine = wines[target_index]   # 현재 와인
  if not wine:
    # 와인이 없다면 
    # window가 size = 3이라면 최대값을, 아니라면 원소 합을 maxV에 더하기
    maxV += max(window) if len(window) == 3 else sum(window)
    window = [] 
    continue
  if len(window) < 2: # window size가 2 미만이라면 와인 추가
    window.append(wine)
    continue
  
  if len(window) < 3:
    window = [window[0], window[1], window[0] + window[1]]
  
  for record_index in range(3):
    if guard == record_index:       # guard에 해당하는 index에는 현재 wine을 더할 수 없음(연속으로 마실 수 없기 때문)
      continue
    window[record_index] += wine    
  guard -= 1
  if guard < 0:
    guard = 2


maxV += max(window) if len(window) == 3 else sum(window)
print(maxV)

