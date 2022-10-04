# 2차원 행렬 

## python으로 2차원 행렬을 다루는 방법



### 2차원 행렬 생성

- python list comprehension 이용
  - python은 comprehension 문법에 특화되어 있기 때문에 실행 시간에서 이점을 가질 수 있다.

```python
# n x n 행렬 생성
matrix = [[0] * n for _ in range(n)]
matrix = [[0 for _ in range(n)] for _ in range(n)]

# 열의 요소가 1, 2, 3, 4, 5 인 행렬을 4행 만들기
matrix = [[i for i in range(1, 6)] for _ in range(4)]

```



### 2차원 행렬 회전

- 90도 회전, 180도 회전, 240도 시계방향 회전

- 기본적으로 90도 회전을 2번 180도,  3번하면 240도 회전이 가능하다.
  - 다만 시간이 그만큼 더 오래 걸리므로 zip 함수 등을 이용할 것이 아니라면 별개 알고리즘으로 구현하는 것이 좋다.

```python
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
                arr[j][n - 1 - i] = arr[i][j]
	# 180도 회전
    if angle == 2:
        for i in range(n):
            for j in range(n):
                arr[n - 1 - i][n - 1 - j] = arr[i][j]
    
    # 270 도 회전
    if angle == 3:
        for i in range(n):
            for j in range(n):
                arr[n - 1 - j][i] = arr[i][j]
    return arr


print(rotate(matrix, 90, n)) # [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]
print(rotate(matrix, 180, n))
print(rotate(matrix, 270, n))

```



#### python zip 함수를 이용하는 방법

- 시계 방향, 반시계방향으로 90도 회전

```python
def rotate_with_zip(matrix, angle = 90):
    arr = list(map(list, zip(*matrix[::-1])))   # 시계 방향
    arr2 = list(map(list, zip(*matrix)))[::-1]  # 반시계 방향
    return arr, arr2

clock, counter_clock = rotate_with_zip(matrix)
print('시계방향 회전: ', clock)
print('반시계방향 회전: ', counter_clock)
```





## 2차원 행렬의 행과 열 전환(전치행렬) 구현

- python zip을 이용하여 간단히 구현 가능

```python
def transform(matrix):
    arr = list(map(list, zip(*matrix)))
    return arr

print(transform(matrix))
```



