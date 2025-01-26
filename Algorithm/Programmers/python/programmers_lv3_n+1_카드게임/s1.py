'''
시간 초과...

'''

'''
목표한 값에 해당하는 카드 두 장을 탐색

1. table의 1 ~ (goal // 2) 까지 탐색
2. table[i] 와 table[goal - i] 가 모두 true 이면 -> 두 카드 쌍을 반환

'''


def search(table, goal):
    for k in range(1, goal // 2 + 1):
        if table[k] and table[goal - k]:
            return (k, goal - k)
    return None


def game(cards, draw_idx, coin, goal, trial=1):
    global maxV, table

    # 더 뽑을 카드 뭉치가 없으면 back
    if draw_idx + 1 >= len(cards):
        maxV = max(maxV, trial)
        return

    # 카드 2장 드로우
    new1, new2 = draw_idx, draw_idx + 1
    draw_idx += 2

    new_card1, new_card2 = cards[new1], cards[new2]

    if coin > 0:
        # case 1. 코인 하나를 소모하여 카드 하나를 갖는다.
        table[new_card1] = True
        # 현재 카드를 가질 때, pair가 있는지 탐색
        pair = search(table, goal)
        if pair:
            # 페어를 버리고 다음 라운드 진행
            table[pair[0]] = False
            table[pair[1]] = False
            game(cards, draw_idx, coin - 1, goal, trial + 1)
            table[pair[0]] = True
            table[pair[1]] = True

        table[new_card1] = False

        table[new_card2] = True
        pair = search(table, goal)
        if pair:
            table[pair[0]] = False
            table[pair[1]] = False
            game(cards, draw_idx, coin - 1, goal, trial + 1)
            table[pair[0]] = True
            table[pair[1]] = True
        table[new_card2] = False

        if coin >= 2:
            # case 2. 코인 두개를 소모하여 카드 두개를 갖는다.
            table[new_card1] = True
            table[new_card2] = True
            pair = search(table, goal)
            if pair:
                table[pair[0]] = False
                table[pair[1]] = False
                game(cards, draw_idx, coin - 2, goal, trial + 1)
                table[pair[0]] = True
                table[pair[1]] = True

            table[new_card1] = False
            table[new_card2] = False

    # case 3. 뽑은 카드를 모두 버린다. -> 아무것도 갖지 않는다.
    pair = search(table, goal)
    if pair:
        table[pair[0]] = False
        table[pair[1]] = False
        game(cards, draw_idx, coin, goal, trial + 1)
        table[pair[0]] = True
        table[pair[1]] = True

    maxV = max(maxV, trial)

    return


def solution(coin, cards):
    global maxV, table
    goal = len(cards) + 1
    maxV = 0
    table = [False] * (len(cards) + 1)  # 카드 값을 index로 하는 계수 리스트
    initial = len(cards) // 3

    # 카드 초기화
    for i in range(initial):
        table[cards[i]] = True

    draw_idx = initial
    game(cards, draw_idx, coin, goal)

    return maxV
