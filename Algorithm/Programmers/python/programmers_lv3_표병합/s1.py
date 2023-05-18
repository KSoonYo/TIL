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

