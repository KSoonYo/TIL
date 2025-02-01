function solution(board, skill) {
  var answer = 0;
  const [n, m] = [board.length, board[0].length];
  const arr = Array(n + 1)
    .fill(0)
    .map(() => Array(m + 1).fill(0));

  skill.forEach(([typ, r1, c1, r2, c2, degree]) => {
    let effect = 0;
    if (typ === 1) {
      effect -= degree;
    } else {
      effect += degree;
    }
    arr[r1][c1] += effect;
    arr[r1][c2 + 1] -= effect;
    arr[r2 + 1][c1] -= effect;
    arr[r2 + 1][c2 + 1] += effect;
  });

  // 가로로 누적합
  for (let r = 0; r < n; r++) {
    for (let c = 1; c < m; c++) {
      arr[r][c] += arr[r][c - 1];
    }
  }

  // 세로로 누적합
  for (let c = 0; c < m; c++) {
    for (let r = 1; r < n; r++) {
      arr[r][c] += arr[r - 1][c];
    }
  }

  // board 파괴되지 않은 건물 집계
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      board[i][j] += arr[i][j];
      if (board[i][j] > 0) {
        answer++;
      }
    }
  }

  return answer;
}
