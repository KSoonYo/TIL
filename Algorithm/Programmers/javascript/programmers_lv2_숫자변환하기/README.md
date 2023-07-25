# 문제

https://school.programmers.co.kr/learn/courses/30/lessons/154538

# 풀이

- 단순 dp 풀이

```js
function solution(x, y, n) {
  const dp = Array.from(new Array(y + 1), () => 1000001);
  dp[x] = 0;
  for (let i = x; i < dp.length; i++) {
    if (i !== x && dp[i] === 1000001) {
      continue;
    }

    if (i + n < dp.length) {
      dp[i + n] = Math.min(dp[i] + 1, dp[i + n]);
    }
    if (i * 2 < dp.length) {
      dp[2 * i] = Math.min(dp[i] + 1, dp[2 * i]);
    }
    if (i * 3 < dp.length) {
      dp[3 * i] = Math.min(dp[i] + 1, dp[3 * i]);
    }
  }

  if (dp[y] === 1000001) {
    return -1;
  }

  return dp[y];
}
```
