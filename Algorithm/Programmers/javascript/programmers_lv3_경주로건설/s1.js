// 테스트 케이스 통과, 최종 fail -> 2처원이 아닌 방향까지 고려하여 3차원으로 풀어야 함
// https://school.programmers.co.kr/questions/30355

function solution(board) {
  var answer = 0;
  const N = board.length;
  const dist = Array.from(new Array(N), () => Array(N).fill(Infinity));
  dist[0][0] = 0;
  const q = [["", [0, 0]]]; // [방향 상태, [r, c]]

  const dirs = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
  ]; // 상, 하, 좌, 우
  while (q.length > 0) {
    const [prevStatus, pos] = q.shift();
    const [r, c] = pos;

    for (const [idx, dir] of dirs.entries()) {
      const [nr, nc] = [r + dir[0], c + dir[1]];
      if (0 <= nr && nr < N && 0 <= nc && nc < N && board[nr][nc] !== 1) {
        let totalCost = dist[r][c] + 100;

        // 기존 방향과 다른 경우 corner cost check
        const cornerCost = 500;
        const nextStatus = idx === 0 || idx === 1 ? "vertical" : "horizon";
        if (
          (nextStatus === "vertical" && prevStatus === "horizon") ||
          (nextStatus === "horizon" && prevStatus === "vertical")
        ) {
          totalCost += cornerCost;
        }
        if (dist[nr][nc] >= totalCost) {
          dist[nr][nc] = totalCost;
          q.push([nextStatus, [nr, nc]]);
        }
      }
    }
  }
  answer = dist[N - 1][N - 1];
  return answer;
}
