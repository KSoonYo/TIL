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
