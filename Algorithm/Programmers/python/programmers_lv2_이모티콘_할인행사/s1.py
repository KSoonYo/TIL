def search(n, users, emoticons, table, i = 0):
    global maxC, maxE

    if i == n:
        cnt = 0
        total = 0
        for u in range(len(table)):
            if table[u] >= users[u][1]:
                cnt += 1
            else:
                total += table[u]
        if cnt > maxC:
            maxC = cnt
            maxE = total
        elif cnt == maxC:
            maxE = max(maxE, total)
        
        return

    for ratio in [10, 20, 30, 40]:
        price = emoticons[i] - (emoticons[i] * (ratio / 100))
        for idx in range(len(users)):                              # 현재 할인 비율을 포함하는 유저 탐색
            stand_disc, stand_price = users[idx]
            if stand_disc <= ratio:
                table[idx] += int(price)
        search(n, users, emoticons, table, i + 1)
        for idx in range(len(users)):                                 
            stand_disc, stand_price = users[idx]
            if stand_disc <= ratio:
                table[idx] -= int(price)


def solution(users, emoticons):
    global maxC, maxE
    n = len(emoticons)
    table =  [0] * len(users)
    maxC, maxE = 0, 0
    search(n, users, emoticons, table)
    answer = [maxC, maxE]
    return answer