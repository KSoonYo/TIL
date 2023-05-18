# 문제 설명
당신은 표 편집 프로그램을 작성하고 있습니다.

표의 크기는 50 × 50으로 고정되어있고 초기에 모든 셀은 비어 있습니다.
각 셀은 문자열 값을 가질 수 있고, 다른 셀과 병합될 수 있습니다.

위에서 r번째, 왼쪽에서 c번째 위치를 (r, c)라고 표현할 때, 당신은 다음 명령어들에 대한 기능을 구현하려고 합니다.

**"UPDATE r c value"**
(r, c) 위치의 셀을 선택합니다.
선택한 셀의 값을 value로 바꿉니다.

**"UPDATE value1 value2"**

value1을 값으로 가지고 있는 모든 셀을 선택합니다.
선택한 셀의 값을 value2로 바꿉니다.

**"MERGE r1 c1 r2 c2"**

(r1, c1) 위치의 셀과 (r2, c2) 위치의 셀을 선택하여 병합합니다.
선택한 두 위치의 셀이 같은 셀일 경우 무시합니다.

선택한 두 셀은 서로 인접하지 않을 수도 있습니다. 이 경우 (r1, c1) 위치의 셀과 (r2, c2) 위치의 셀만 영향을 받으며, 그 사이에 위치한 셀들은 영향을 받지 않습니다.

두 셀 중 한 셀이 값을 가지고 있을 경우 병합된 셀은 그 값을 가지게 됩니다.

두 셀 모두 값을 가지고 있을 경우 병합된 셀은 (r1, c1) 위치의 셀 값을 가지게 됩니다.

이후 (r1, c1) 와 (r2, c2) 중 어느 위치를 선택하여도 병합된 셀로 접근합니다.

**"UNMERGE r c"**

(r, c) 위치의 셀을 선택하여 해당 셀의 모든 병합을 해제합니다.
선택한 셀이 포함하고 있던 모든 셀은 프로그램 실행 초기의 상태로 돌아갑니다.

병합을 해제하기 전 셀이 값을 가지고 있었을 경우 (r, c) 위치의 셀이 그 값을 가지게 됩니다.

**"PRINT r c"**

(r, c) 위치의 셀을 선택하여 셀의 값을 출력합니다.
선택한 셀이 비어있을 경우 "EMPTY"를 출력합니다.

아래는 UPDATE 명령어를 실행하여 빈 셀에 값을 입력하는 예시입니다.

|commands|효과|
|--------|---|
|UPDATE 1 1 menu	|(1,1)에 "menu" 입력|
UPDATE 1 2 category	|(1,2)에 "category" 입력
UPDATE 2 1 bibimbap	|(2,1)에 "bibimbap" 입력
UPDATE 2 2 korean	|(2,2)에 "korean" 입력
UPDATE 2 3 rice	|(2,3)에 "rice" 입력
UPDATE 3 1 ramyeon	|(3,1)에 "ramyeon" 입력
UPDATE 3 2 korean	|(3,2)에 "korean" 입력
UPDATE 3 3 noodle	|(3,3)에 "noodle" 입력
UPDATE 3 4 instant	|(3,4)에 "instant" 입력
UPDATE 4 1 pasta	|(4,1)에 "pasta" 입력
UPDATE 4 2 italian	|(4,2)에 "italian" 입력
UPDATE 4 3 noodle	|(4,3)에 "noodle" 입력

위 명령어를 실행하면 아래 그림과 같은 상태가 됩니다.

![](./assets/2023-05-18-12-10-29.png)

아래는 MERGE 명령어를 실행하여 셀을 병합하는 예시입니다.

|commands|	효과|
|--------|-----|
MERGE 1 2 1 3	|(1,2)와 (1,3) 병합
MERGE 1 3 1 4	|(1,3)과 (1,4) 병합

위 명령어를 실행하면 아래와 같은 상태가 됩니다.

![](./assets/2023-05-18-12-11-46.png)

병합한 셀은 "category" 값을 가지게 되며 (1,2), (1,3), (1,4) 중 어느 위치를 선택하더라도 접근할 수 있습니다.

아래는 UPDATE 명령어를 실행하여 셀의 값을 변경하는 예시입니다.

|commands	|효과|
|-----------|---|
UPDATE korean hansik	|"korean"을 "hansik"으로 변경
UPDATE 1 3 group	|(1,3) 위치의 셀 값을 "group"으로 변경

위 명령어를 실행하면 아래와 같은 상태가 됩니다.


아래는 UNMERGE 명령어를 실행하여 셀의 병합을 해제하는 예시입니다.

|commands|	효과|
|--------|------|
UNMERGE 1 4	|셀 병합 해제 후 원래 값은 (1,4)가 가짐

위 명령어를 실행하면 아래와 같은 상태가 됩니다.

![](./assets/2023-05-18-12-13-24.png)

실행할 명령어들이 담긴 1차원 문자열 배열 commands가 매개변수로 주어집니다.

 commands의 명령어들을 순서대로 실행하였을 때, "PRINT r c" 명령어에 대한 실행결과를 순서대로 1차원 문자열 배열에 담아 return 하도록 solution 함수를 완성해주세요.


## 제한사항
- 1 ≤ commands의 길이 ≤ 1,000
  - commands의 각 원소는 아래 5가지 형태 중 하나입니다.
  - "UPDATE r c value"
    - r, c는 선택할 셀의 위치를 나타내며, 1~50 사이의 정수입니다. value는 셀에 입력할 내용을 나타내며, 알파벳 소문자와 숫자로 구성된 길이 1~10 사이인 문자열입니다.
  - "UPDATE value1 value2"
    - value1은 선택할 셀의 값, value2는 셀에 입력할 내용을 나타내며, 알파벳 소문자와 숫자로 구성된 길이 1~10 사이인 문자열입니다.
  - "MERGE r1 c1 r2 c2"
    - r1, c1, r2, c2는 선택할 셀의 위치를 나타내며, 1~50 사이의 정수입니다.
  - "UNMERGE r c"
    - r, c는 선택할 셀의 위치를 나타내며, 1~50 사이의 정수입니다.
  - "PRINT r c"
    - r, c는 선택할 셀의 위치를 나타내며, 1~50 사이의 정수입니다.

commands는 1개 이상의 "PRINT r c" 명령어를 포함하고 있습니다.

### 입출력 예
|commands|	result|
|--------|---------|
["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]	|["EMPTY", "group"]
["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]|["d", "EMPTY"]

---

# 문제 풀이
- union-find로 풀이
  - 임의의 좌표 (i,j)를 병합한 대표 노드를 찾는 find 함수를 구현 
  - 값을 업데이트할 때에는 find 함수로 찾은 대표 노드에 대해서만 값 갱신
  - 병합을 할 때에는 문제 조건에 따라 (r1, c1) 좌표로 (r2, c2) cell을 병합하는 union 함수 구현
  - **병합을 해제할 때 주의점**: 곧바로 병합을 풀어버리면 중간에 링크가 깨질 우려가 있음

```python
def solution(commands):
    answer = []
    table = [['' for _ in range(51)] for _ in range(51)]
    union_map = [[(r,c) for c in range(51)] for r in range(51)]
    
    for command in commands:
        command_set = command.split()
        if command_set[0] == 'UPDATE':
            if len(command_set) > 3:
                r, c = int(command_set[1]), int(command_set[2])
                value = command_set[3]
                tr, tc = find(union_map, (r, c))
                table[tr][tc] = value
            else:
                v1, v2 = command_set[1], command_set[2]
                for i in range(51):
                    for j in range(51):
                        tr, tc = find(union_map, (i, j))
                        if table[tr][tc] == v1:
                            table[tr][tc] = v2
        elif command_set[0] == 'MERGE':
            r1, c1 = map(int, command_set[1:3])
            r2, c2 = map(int, command_set[3:])
            merge(union_map, table, (r1, c1), (r2, c2))
        elif command_set[0] == 'UNMERGE':
            r, c = map(int, command_set[1:])
            target = find(union_map, (r, c))
            unmerge(union_map, table, target, (r, c))
        else:
            r, c = map(int, command_set[1:])
            tr, tc = find(union_map, (r, c))
            if table[tr][tc]:
                answer.append(table[tr][tc])
            else:
                answer.append('EMPTY')
    return answer

def find(union_map, pos):
    r, c = pos
    if union_map[r][c] == pos:
        return pos
    return find(union_map, union_map[r][c])

def merge(union_map, table, pos1, pos2):
    r1, c1 = find(union_map, pos1)
    r2, c2 = find(union_map, pos2)
    if (r1, c1) == (r2, c2):
        return
    
    union_map[r2][c2] = (r1, c1)
    
    if table[r1][c1] and table[r2][c2]:
        table[r2][c2] = table[r1][c1]
    elif table[r1][c1]:
        table[r2][c2] = table[r1][c1]
    else:
        table[r1][c1] = table[r2][c2]
    return

def unmerge(union_map, table, target, pos):
    r, c = pos
    temp = table[target[0]][target[1]]
    rollback = []
    for i in range(1, 51):
        for j in range(1, 51):
            tr, tc = find(union_map, (i, j))
            if (tr, tc) == target:
                rollback.append((i, j))
    for init_r, init_c in rollback:
        union_map[init_r][init_c] = (init_r, init_c)
        table[init_r][init_c] = ''
    table[r][c] = temp
    return



```
