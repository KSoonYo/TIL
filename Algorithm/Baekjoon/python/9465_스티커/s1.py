case = int(input())
case_num = 0
final_result = []

while case_num < case:
    num = int(input())
    num_list = [[0 for i in range(num)] for j in range(2)]
    num_list[0] = list(map(int, input().split()))
    num_list[1] = list(map(int, input().split())) 
    
    if num > 1:
        num_list[0][1] += num_list[1][0]
        num_list[1][1] += num_list[0][0]

    for h in range(2, num):
        num_list[0][h] += max(num_list[1][h-1], num_list[1][h-2])
        num_list[1][h] += max(num_list[0][h-1], num_list[0][h-2])
    final_result.append(max(num_list[0][num-1], num_list[1][num-1]))
    case_num += 1

for k in range(len(final_result)):
    print(final_result[k])