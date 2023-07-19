# 문제

https://school.programmers.co.kr/learn/courses/30/lessons/42884

# 풀이

- 차가 진입하는 시간 순대로 정렬(오름차순)
  - 먼저 진입한 차가 나가기 전에 다른 차가 진입했다면, 그것은 하나의 구간으로 볼 수 있음
    - ex) `car1: [-20, -10]` 와 `car2: [-17, -15]` 가 있다면 car2는 car1이 나가기 전에 진입했으므로 두 차량이 겹치는 구간이 곧 카메라 설치가 가능한 구간
- 중요) 먼저 진입한 차량이라도 다음에 진입한 차량보다 늦게 나갈 수 있다.(위 예시 참고)
- 구간의 마지막(차량이 나가는 시간)은 구간 내에서 진입한 차량들 중 빨리 나가는 차량의 시간으로 갱신해줘야 한다.
  - 구간의 마지막을 빨리 나가는 시간으로 설정해줘야 카메라 설치 가능한 공간이 분리되기 때문

```js
function solution(routes) {
  var answer = 1;

  // sort by routes[i][0]
  // 오름차순(진입이 빠른 순대로 정렬)
  routes.sort((a, b) => a[0] - b[0]);

  stack = [];

  for (const [carIn, carOut] of routes) {
    if (stack.length === 0) {
      stack.push([carIn, carOut]);
      continue;
    }
    const lastIdx = stack.length - 1;
    if (carIn <= stack[lastIdx][1]) {
      // 새로 들어오는 차량의 진입 시간이 이전에 있던 차량이 나가는 시간 이내라면 -> 같은 구간
      stack[lastIdx][1] = Math.min(carOut, stack[lastIdx][1]); // 중요: 최종 나가는 시간 갱신(구간 갱신)
    } else {
      // 이전 구간 마지막 시간 이후로 새로 차량이 들어왔다면 -> 다른 구간
      stack.push([carIn, carOut]);
    }
  }

  return stack.length;
}
```
