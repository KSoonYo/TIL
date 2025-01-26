# 문제

https://school.programmers.co.kr/learn/courses/30/lessons/181188

# 풀이

## 문제 이해

- A나라가 발사한 미사일은 x 축에 평행한 직선 구간으로 표현됨
- 각 미사일은 [s, e] 형태로 주어지며, s는 시작 위치, e는 끝 위치
- B나라는 특정 x좌표에서 y축에 수평이 되도록 미사일을 발사
- 요격 미사일은 발사 위치에서 일직선으로 위로 발사되며, 그 경로 안에 있는 모든 미사일을 요격

## 해결 방법

1. **미사일 정렬**

   - 시작 지점을 기준으로 오름차순 정렬
   - 시작 지점이 같다면 끝 지점을 기준으로 정렬

2. **요격 위치 선정**
   - lastEnd 변수로 현재까지의 요격 가능한 최소 끝점을 관리
   - 새로운 미사일을 검사할 때:
     - 현재 미사일의 시작점이 lastEnd보다 작으면 (겹치는 구간)
       - 현재 미사일의 끝점이 더 작으면 lastEnd 갱신 (더 효율적인 요격 지점)
     - 현재 미사일의 시작점이 lastEnd보다 크거나 같으면
       - 새로운 요격 미사일 필요
       - lastEnd를 현재 미사일의 끝점으로 갱신

## 코드

```javascript
function solution(targets) {
  var answer = 0;
  targets.sort((a, b) => {
    if (a[0] !== b[0]) {
      return a[0] - b[0];
    }
    return a[1] - b[1];
  });

  let lastEnd = -1;

  targets.forEach((target) => {
    const [s, e] = target;
    if (lastEnd < 0) {
      lastEnd = e;
      return;
    }
    if (s < lastEnd) {
      if (e < lastEnd) {
        lastEnd = e;
      }
      return;
    }
    lastEnd = e;
    answer++;
  });

  return answer + 1;
}
```
