# 문제
https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

# 풀이
- 핵심) ranked는 내림차순 정렬, player는 오름차순 정렬
  - player의 점수의 순서를 중복을 제거한 ranked 배열의 끝 요소부터 비교하면서 i번째 수가 현재 player의 점수보다 낮거나 같은 경우를 체크하여 break
    - ranked의 i번째 점수보다 현재 score가 작다면 score는 i + 1번째에 위치한 점수가 된다.(ranked가 내림차순 정렬이기 때문)
    - ranked의 i번째 점수가 현재 score와 같다면 score는 ranked의 i 등수를 그대로 따라간다.
  - 만약 ranked의 0번째 점수보다 player의 점수가 더 높다면 player의 등수는 항상 1등(player는 오름차순이기 때문에 현재 ranked보다 더 높은 점수를 받았다면 그 이후부터는 항상 1등이다.) 
  - i가 0일때 맨 앞이기 때문에 구한 rank에서 1을 추가로 더해준다.
- 이진탐색으로도 풀이 가능
```ts
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

```