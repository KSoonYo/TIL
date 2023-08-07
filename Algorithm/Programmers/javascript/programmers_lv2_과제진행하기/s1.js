function solution(plans) {
  var answer = [];

  const sortedPlans = plans
    .map(([task, time, process]) => {
      const [hour, minute] = time.split(":");

      return [task, parseInt(hour) * 60 + parseInt(minute), parseInt(process)];
    })
    .sort((a, b) => a[1] - b[1]);

  const stack = [];
  let time = sortedPlans[0][1] + sortedPlans[0][2]; // 이전 작업의 완료 예정 시간
  for (let i = 1; i < sortedPlans.length; i++) {
    const [task, startTime, process] = sortedPlans[i];
    if (startTime < time) {
      stack.push([sortedPlans[i - 1][0], time - startTime]);
      time = startTime + process;
    } else if (startTime === time) {
      answer.push(sortedPlans[i - 1][0]);
      time = startTime + process;
    } else {
      answer.push(sortedPlans[i - 1][0]);

      let blank = startTime - time;
      let recent = stack.length - 1;
      while (stack.length > 0) {
        if (stack[recent][1] <= blank) {
          blank -= stack[recent][1];
          answer.push(stack.pop()[0]);
          recent = stack.length - 1;
          continue;
        }
        stack[recent][1] -= blank;
        break;
      }

      time = startTime + process;
    }
  }
  // 가장 마지막 작업 추가
  answer.push(sortedPlans[sortedPlans.length - 1][0]);
  while (stack.length > 0) {
    // stack에 남은 작업 모두 추가
    answer.push(stack.pop()[0]);
  }
  return answer;
}
