
def unlock(char_index:int, chars: str = '', moum_cnt = 0, zaum_cnt = 0):
  global l, c, moum_table, alphabets

  # 길이 개수와 암호 조건 개수를 충족하면 암호문 출력
  if len(chars) == l:
    if moum_cnt >= 1 and zaum_cnt >= 2:
      print(chars)
    return

  for next_index in range(char_index + 1, c):
    next_char = alphabets[next_index]
    if next_char in moum_table:
      unlock(next_index, chars + next_char,  moum_cnt + 1, zaum_cnt)
    else:
      unlock(next_index, chars + next_char,  moum_cnt, zaum_cnt + 1)
  return


l, c = map(int, input().split())
alphabets = input().split()
alphabets.sort()

moum_table = set(['a', 'e', 'i', 'o', 'u'])

for i in range(c):
  start_char = alphabets[i]
  if start_char in moum_table:
    unlock(i, start_char,  1, 0)
  else:
    unlock(i, start_char,  0, 1)
