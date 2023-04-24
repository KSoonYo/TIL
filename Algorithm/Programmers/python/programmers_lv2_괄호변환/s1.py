def check(w):
    stack = []
    for c in w:
        if len(stack) == 0 and c == ")":
            return False
        if c == "(":
            stack.append(c)
        else:
            stack.pop()
    if stack:
        return False
    return True

def reverse(w):
    reverse_table = {"(" : ")", ")": "("}
    reversed_w = ""
    for blank in w:
        reversed_w += reverse_table[blank]
    return reversed_w
def main(p):
    result = ""
    if check(p):
        return p
    table = {"(" : 0, ")" : 0}
    for i in range(len(p)):
        h = p[i]
        table[h] += 1
        if table["("] == table[")"]:
            u, v = p[:i+1], p[i+1:]
            if check(u):
                result = u + main(v)
            else:
                result = "(" + main(v) + ")" + reverse(u[1:i])
            return result
    return ""

def solution(p):
    answer = main(p)
    return answer