function solution(sequence, k) {
  // sequence -> 오름차순 정렬
  var answer = [];
  var [p1, p2] = [0, 0];
  var temp = sequence[p1];
  while (p1 < sequence.length && p2 < sequence.length) {
    if (temp > k) {
      temp -= sequence[p1];
      p1++;
    } else if (temp === k) {
      var newLength = p2 - p1 + 1;
      if (answer.length === 0 || newLength < answer[1] - answer[0] + 1) {
        answer = [p1, p2];
      }
      temp -= sequence[p1];
      p1++;
    } else {
      if (p2 + 1 > sequence.length) {
        break;
      }
      temp += sequence[p2 + 1];
      p2++;
    }
  }

  return answer;
}
