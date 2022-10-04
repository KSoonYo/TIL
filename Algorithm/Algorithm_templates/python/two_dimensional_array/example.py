n = 4
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

# 회전
def rotate(n, matrix, angle):
    arr = [[0] * n for _ in range(n)]
  	
    # 90, 180, 270, 360 ... 등 90의 배수가 아니라면 return 
    if angle % 90:
        return
    angle = (angle // 90) % 4
	
    # 360도 회전 -> 받은 배열 그대로
    if angle == 0:
        return matrix
    
    # 90도 회전
    if angle == 1:        
        for i in range(n):
            for j in range(n):
                arr[j][n - 1 - i] = matrix[i][j]
	# 180도 회전
    if angle == 2:
        for i in range(n):
            for j in range(n):
                arr[n - 1 - i][n - 1 - j] = matrix[i][j]
    
    # 270 도 회전
    if angle == 3:
        for i in range(n):
            for j in range(n):
                arr[n - 1 - j][i] = matrix[i][j]
    return arr


print(rotate(matrix, 90, n)) # [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]
print(rotate(matrix, 180, n)) # [[16, 15, 14, 13], [12, 11, 10, 9], [8, 7, 6, 5], [4, 3, 2, 1]]
print(rotate(matrix, 270, n)) # [[4, 8, 12, 16], [3, 7, 11, 15], [2, 6, 10, 14], [1, 5, 9, 13]]



def rotate_with_zip(matrix, angle = 90):
    arr = list(map(list, zip(*matrix[::-1])))   # 시계 방향
    arr2 = list(map(list, zip(*matrix)))[::-1]  # 반시계 방향
    return arr, arr2

clock, counter_clock = rotate_with_zip(matrix)
print('시계방향 회전: ', clock)
print('반시계방향 회전: ', counter_clock)


# 전치행렬 전환
def transform(matrix):
    arr = list(map(list, zip(*matrix)))
    return arr

print(transform(matrix))