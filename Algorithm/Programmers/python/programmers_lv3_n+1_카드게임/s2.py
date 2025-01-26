
def solution(coin, cards):
    goal = len(cards) + 1
    turn = 0
    initial_length = len(cards) // 3
    initial = [cards[i] for i in range(initial_length)]
    drawn = []
    gone = [False] * 1001

    idx = initial_length
    while True:
        done = False
        turn += 1

        # 카드 뭉치를 모두 소진한 경우, 게임 종료
        if idx >= len(cards):
            break

        drawn.append(cards[idx])
        drawn.append(cards[idx + 1])
        idx += 2

        # 기존 카드 중에서 매칭이 되는 경우 탐색
        for i in range(len(initial)):
            if gone[initial[i]]:
                continue
            for j in range(i + 1, len(initial)):
                card1, card2 = initial[i], initial[j]
                if not gone[card1] and not gone[card2] and card1 + card2 == goal:
                    gone[card1] = True
                    gone[card2] = True
                    done = True
                    break
            if done:
                break

        # 위의 경우에서 해결 되었다면 다음 턴 진행
        if done:
            continue

        # 기존 카드와 새로 뽑은 카드가 짝이 되는 경우 탐색
        # 매칭이 되면 코인 1개 소모
        for init_card in initial:
            if coin <= 0:
                break
            if gone[init_card]:
                continue
            for drawn_card in drawn:
                if not gone[init_card] and not gone[drawn_card] and init_card + drawn_card == goal:
                    gone[init_card] = True
                    gone[drawn_card] = True
                    coin -= 1
                    done = True
                    break
            if done:
                break

        # 위에서 해결 되었다면 다음 턴 진행
        if done:
            continue

        # 새로 뽑은 카드 중에서 짝이 되는 경우 탐색
        # 매칭이 되면 코인 2개 소모
        for k in range(len(drawn)):
            card1 = drawn[k]
            if coin <= 1:
                break
            if gone[card1]:
                continue
            for h in range(k + 1, len(drawn)):
                card2 = drawn[h]
                if not gone[card2] and card1 + card2 == goal:
                    gone[card1] = True
                    gone[card2] = True
                    coin -= 2
                    done = True
                    break
            if done:
                break

        # 위의 세 가지 경우로도 n + 1을 못 만들면 그대로 게임 끝
        if not done:
            break

    return turn
