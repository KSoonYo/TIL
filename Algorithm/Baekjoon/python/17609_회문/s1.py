def is_palindrome(target):

    p1 = 0
    p2 = len(target) - 1

    unbalanced_set = set()

    is_full_palindrome = True
    while p1 <= p2:
        s1, s2 = target[p1], target[p2]

        # 양쪽 끝 문자열이 다른 경우
        if s1 != s2:
            is_full_palindrome = False
            unbalanced_set.add(p1)
            unbalanced_set.add(p2)
            break

        p1 += 1
        p2 -= 1

    # 완전한 회문인 경우
    if is_full_palindrome:
        return 0

    is_semi_palindrome = False
    for k in unbalanced_set:
        flag = True
        c1 = 0
        c2 = len(target) - 1
        while c1 <= c2:
            if c1 == k:
                c1 += 1
                continue
            if c2 == k:
                c2 -= 1
                continue
            s1, s2 = target[c1], target[c2]
            if s1 != s2:
                flag = False
                break
            c1 += 1
            c2 -= 1
        if flag:
            is_semi_palindrome = True
            break

    if is_semi_palindrome:
        return 1
    return 2


T = int(input())

results = []
for _ in range(T):
    string = input()
    results.append(is_palindrome(string))

for result in results:
    print(result)
