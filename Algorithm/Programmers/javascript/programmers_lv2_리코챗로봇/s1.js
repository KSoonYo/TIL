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
