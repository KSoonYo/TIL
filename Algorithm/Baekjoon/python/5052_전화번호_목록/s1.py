t = int(input())

for _ in range(t):
    n = int(input())
    phone_numbers = []
    for i in range(n):
        phone_numbers.append(input())

    phone_numbers.sort(key=lambda x: (x, len(x)))
    for k in range(len(phone_numbers) - 1):
        phone_number = phone_numbers[k]
        target = phone_numbers[k + 1]
        if target.startswith(phone_number):
            print("NO")
            break
    else:
        print("YES")
