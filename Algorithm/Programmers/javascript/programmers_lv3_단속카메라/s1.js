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
