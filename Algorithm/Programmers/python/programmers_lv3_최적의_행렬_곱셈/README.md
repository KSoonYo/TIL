# 문제
https://school.programmers.co.kr/learn/courses/30/lessons/12942#

크기가 a by b인 행렬과 크기가 b by c 인 행렬이 있을 때, 두 행렬을 곱하기 위해서는 총 a x b x c 번 곱셈해야합니다.
예를 들어서 크기가 5 by 3인 행렬과 크기가 3 by 2인 행렬을 곱할때는 총 5 x 3 x 2 = 30번의 곱하기 연산을 해야 합니다.

행렬이 2개일 때는 연산 횟수가 일정 하지만, 행렬의 개수가 3개 이상일 때는 연산의 순서에 따라서 곱하기 연산의 횟수가 바뀔 수 있습니다. 

예를 들어서 크기가 5 by 3인 행렬 A, 크기가 3 by 10인 행렬 B, 크기가 10 by 6인 행렬 C가 있을 때, 순서대로 A와 B를 먼저 곱하고, 그 결과에 C를 곱하면 A와 B행렬을 곱할 때 150번을, AB 에 C를 곱할 때 300번을 연산을 해서 총 450번의 곱하기 연산을 합니다. 하지만, B와 C를 먼저 곱한 다음 A 와 BC를 곱하면 180 + 90 = 270번 만에 연산이 끝납니다.

각 행렬의 크기 matrix_sizes 가 매개변수로 주어 질 때, 모든 행렬을 곱하기 위한 최소 곱셈 연산의 수를 return하는 solution 함수를 완성해 주세요.

## 제한 사항
행렬의 개수는 3이상 200이하의 자연수입니다.

각 행렬의 행과 열의 크기는 200이하의 자연수 입니다.

계산을 할 수 없는 행렬은 입력으로 주어지지 않습니다.

## 입출력 예
|matrix_sizes	|result|
|-------------|------|
[[5,3],[3,10],[10,6]]|	270

---

# 풀이
- dp 문제
- 행렬의 연산 결과식은 연산 순서에 상관없이 고정
  - ex) A : 1 x 2 행렬, B : 2 x 5 행렬, C : 5 x 3 행렬
  - (AB) C를 하든, A(BC)를 하든 결과식은 1 X 3
- 이전에 계산한 값을 활용해서 연산 최소값을 갱신
- Top-down(하향식) 방식: 현재 위치 (0, i) 자리의 행렬 연산 결과를 0행의 0열부터 i - 1열, i열의 1행부터 행렬의 개수 N 행까지 dp table에 저장해둔 연산 결과를 활용하여 업데이트
  - 이때 행렬의 연산 순서에 맞는 dp 테이블 내 규칙을 찾는 것이 핵심

```python
def solution(matrix_sizes):
    answer = 0
    n = len(matrix_sizes)
    table = [[[] for _ in range(n)] for _ in range(n)]

    for i in range(n):                                      # 대각선 행렬 채우기
        x, y = 0, i
        for _ in range(n - i):
            if x == y:
                table[x][y] = (0, matrix_sizes[y])          # (연산 횟수, 현재 행렬)
                x, y = x + 1, y + 1
                continue
            if y - x == 1:
                a, b = table[x][y - 1][1], table[x + 1][y][1]
                c = (a[0] * a[1] * b[1], [a[0], b[1]])
                table[x][y] = c
                x, y = x + 1, y + 1
                continue
            for k in range(1, y - x + 1):
                a, b = table[x][y - k][1], table[y - k + 1][y][1]
                c = (table[x][y - k][0] + table[y - k + 1][y][0] + (a[0] * a[1] * b[1]), [a[0], b[1]])
                if table[x][y]:
                    prev = table[x][y]
                    table[x][y] = (min(prev[0], c[0]), c[1])
                else:
                    table[x][y] = c
            x, y = x + 1, y + 1
    answer = table[0][n - 1][0]
    return answer
```

- 비슷한 문제로 백준 11049번 행렬 곱셈 순서가 있다.
- partition으로 구분해서 dp 테이블 내 규칙을 적용한 풀이 방식
```python
import sys
input = sys.stdin.readline

n = int(input())
mats = []
dp = [[[(0, 0), 2 ** 31] for _ in range(n)] for _ in range(n)]            # 인덱스: n - 1번째 행렬, 값: [행렬곱 결과(row, col), 개수]
'''
dp 형태(A: 5x3, B: 3x2, C: 2x6)
        A(0)         B(1)             C(2)
A(0)    A            AxB            AxBxC -> min(A(BC), (AB)C)
    (5, 3), 0 |  (5, 2), 30 |

                     B             BxC
B(1)          |  (3, 2), 0  |     (3, 6), 36

                                    C
C(2)                        |     (2, 6), 0

'''

for _ in range(n):
    r, c = map(int, input().split())
    mats.append((r, c))

for i in range(n):
    # 대각선 순으로 dp 채우기
    s, e = 0, i                     # 시작점 항상 0, 끝점은 i를 따라감
    partition = e - 1               # 분할 기준은 끝점 e보다 1 작음

    while s < n and e < n:
        if s == e:
            # 행렬 1개인 경우
            # 행렬곱 연산 횟수는 0
            dp[s][e][0] = mats[s]
            dp[s][e][1] = 0
        else:
            # 1) 행렬곱 연산결과 저장
            # 행렬곱의 연산결과는 dp 상 현재 위치에서 (s, partition) 행렬의 첫번째 인자와 (partition + 1, e)의 두번째 인자로 이루어짐
            # 즉 dp의 현재 위치에서 왼쪽에 있는 행렬곱 연산결과의 0번째, 아래쪽에 있는 행렬곱 연산결과의 1번째 인자를 취함  
            dp[s][e][0] = (dp[s][partition][0][0], dp[partition + 1][e][0][1])

            # 2) 행렬곱 연산횟수 저장
            # 시작점에서 partition 까지(즉 현재 위치에서 한 칸 왼쪽 column index, 한 칸 아래쪽 row index에 있는 행렬 위치까지)
            # 행렬곱 연산횟수 최소값 갱신
            for j in range(s, partition + 1):
                dp[s][e][1] = min(dp[s][e][1], dp[s][j][1] + dp[j + 1][e][1] + (dp[s][j][0][0] * dp[j + 1][e][0][0] * dp[j + 1][e][0][1]))
        s += 1
        e += 1
        partition = e - 1

print(dp[0][n-1][1])
```
