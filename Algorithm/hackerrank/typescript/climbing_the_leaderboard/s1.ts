function climbingLeaderboard(ranked: number[], player: number[]): number[] {
  const answer: number[] = [];
  const board = [...new Set(ranked)].sort((a, b) => b - a);
  player.forEach((score) => {
    let rank = 0;
    for (let i = board.length - 1; i >= 0; i--) {
      if (score > board[0]) {
        rank = 1;
        break;
      }
      if (score < board[i]) {
        rank = i + 1;
        break;
      } else if (score === board[i]) {
        rank = i;
        break;
      }
    }
    answer.push(rank + 1);
  });
  return answer;
}
