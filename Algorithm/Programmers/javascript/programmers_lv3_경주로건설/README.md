# 문제

https://school.programmers.co.kr/learn/courses/30/lessons/67259

# 풀이

- 3차원 dp + bfs

  - 방향을 고려해야하는 이유?
    - 벽, 코너로 인해 이전에 특정 방향으로 최소치를 갱신한 곳이라 하더라도 다른 방향에서 해당 위치에 재방문했을 때 최소 비용이 업데이트할 수 있기 때문
    - 즉 이미 방문한 곳이라도 다시 방문했을 때 비용이 더 낮은 경우가 생긴다면 재방문을 해야한다. -> 해당 위치에 도착한 모든 방향에 대해 비용을 기록해놓을 필요가 있음
    - `dp[행 위치][열 위치][방향]`

```js
// 3차원 dp 풀이

function solution(board) {
  const N = board.length;

  const dist = Array(N)
    .fill(0)
    .map((_) =>
      Array.from(new Array(N), () => [Infinity, Infinity, Infinity, Infinity])
    );
  dist[0][0] = [0, 0, 0, 0];
  const dirs = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
  ]; // 상, 하, 좌, 우
  const q = []; // [r, c, cost, dir]

  // 시작은 아래쪽, 오른쪽부터
  if (board[1][0] === 0) {
    q.push([1, 0, 100, 1]);
    dist[1][0][1] = 100;
  }

  if (board[0][1] === 0) {
    q.push([0, 1, 100, 3]);
    dist[0][1][3] = 100;
  }

  while (q.length > 0) {
    const [r, c, cost, dir] = q.shift();

    for (const [idx, ndir] of dirs.entries()) {
      let nextCost = 100;
      const [nr, nc] = [r + ndir[0], c + ndir[1]];
      const prevStatus = dir === 0 || dir === 1 ? "vertical" : "horizon";
      const nextStatus = idx === 0 || idx === 1 ? "vertical" : "horizon";

      if (0 <= nr && nr < N && 0 <= nc && nc < N && board[nr][nc] !== 1) {
        if (
          (prevStatus === "vertical" && nextStatus === "horizon") ||
          (prevStatus === "horizon" && nextStatus === "vertical")
        ) {
          nextCost += 500;
        }
        if (dist[nr][nc][idx] > cost + nextCost) {
          dist[nr][nc][idx] = cost + nextCost;
          q.push([nr, nc, cost + nextCost, idx]);
        }
      }
    }
  }
  return Math.min(...dist[N - 1][N - 1]);
}
```

- 응용 문제: [빛의 경로 사이클](https://school.programmers.co.kr/learn/courses/30/lessons/86052)
  - 이미 방문한 사이클은 현재 위치에 같은 방향으로 도달한 적이 있는지를 확인하여 체크 가능
  - 중요한 것은 각각의 위치에 대해 상, 하, 좌, 우 4 방향에 대해 확인하는 것
