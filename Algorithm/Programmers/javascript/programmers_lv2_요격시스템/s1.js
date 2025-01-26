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
