# 문제

https://school.programmers.co.kr/learn/courses/30/lessons/169199

# 풀이

## 주요 로직

1. 초기 설정

   - 상하좌우 이동을 위한 방향 배열 (dr, dc) 정의
   - 시작점(R)과 도착점(G)의 좌표 찾기
   - 방문 체크를 위한 2차원 배열 생성

2. BFS 탐색

   - 큐에 시작점과 이동 횟수(1)를 함께 저장
   - 각 위치에서 4방향으로 미끄러져 이동
   - 미끄러짐은 장애물(D)이나 벽을 만날 때까지 계속됨

3. 이동 처리

   - 각 방향으로 미끄러질 때:
     - 배열 범위를 벗어나거나 장애물을 만날 때까지 직진
     - 멈춘 위치가 목표점(G)이면 현재까지의 이동 횟수 반환
     - 이미 방문한 위치라면 스킵
     - 새로운 위치라면 방문 처리 후 큐에 추가

4. 결과
   - 목표점에 도달하면 이동 횟수 반환
   - 도달할 수 없다면 -1 반환

## 시간 복잡도

- O(N×M×4), N은 보드의 행 개수, M은 열 개수
- 각 칸에서 4방향으로의 이동을 고려

## 공간 복잡도

- O(N×M), 방문 배열의 크기

## 코드

```javascript
// 상, 하, 좌, 우
const dr = [-1, 1, 0, 0];
const dc = [0, 0, -1, 1];

function solution(board) {
  var answer = -1;
  const maxRowLength = board.length;
  const maxColLength = board[0].length;

  const start = [0, 0];
  const goal = [maxRowLength, maxColLength];

  board.forEach((row, rIndex) => {
    for (let cIndex = 0; cIndex < row.length; cIndex++) {
      let target = row[cIndex];
      if (target === "R") {
        start[0] = rIndex;
        start[1] = cIndex;
      }

      if (target === "G") {
        goal[0] = rIndex;
        goal[1] = cIndex;
      }
    }
  });

  const visited = Array(maxRowLength)
    .fill(0)
    .map(() => Array(maxColLength).fill(false));
  visited[start[0]][start[1]] = true;
  const queue = [[...start, 1]]; // (r, c, 회차)

  while (queue.length > 0) {
    const [r, c, cnt] = queue.shift();

    let nr = r;
    let nc = c;

    for (let k = 0; k < 4; k++) {
      // k 방향 결정

      while (0 <= nr && nr < maxRowLength && 0 <= nc && nc < maxColLength) {
        const isEdge =
          0 > nr + dr[k] ||
          nr + dr[k] >= maxRowLength ||
          0 > nc + dc[k] ||
          nc + dc[k] >= maxColLength;
        const isAvailable = !isEdge && board[nr + dr[k]][nc + dc[k]] !== "D";

        // 배열의 끝이 아니고 장애물이 없다면 계속 직진
        if (isAvailable) {
          nr += dr[k];
          nc += dc[k];
          continue;
        }

        // 현재 위치가 배열의 끝이거나 다음 위치에 장애물이 나온다면 현재 위치가 목적지인지 확인 후 방향 전환을 위해 큐에 추가
        if (board[nr][nc] === "G") {
          return cnt;
        } else if (!visited[nr][nc]) {
          visited[nr][nc] = true;
          queue.push([nr, nc, cnt + 1]);
          // 초기화
          nr = r;
          nc = c;
          break;
        } else {
          nr = r;
          nc = c;
          break;
        }
      }
    }
  }
  return answer;
}
```
