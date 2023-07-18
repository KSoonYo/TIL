function solution(r1, r2) {
  var answer = 0;
  // x^2 + y^2 = r^2

  for (let x = 1; x <= r2; x++) {
    let [y1, y2] = [0, 0];
    if (x < r1) {
      y1 = Math.ceil((r1 ** 2 - x ** 2) ** 0.5);
    }
    y2 = Math.floor((r2 ** 2 - x ** 2) ** 0.5) + 1;
    answer += y2 - y1;
  }

  return answer * 4;
}
