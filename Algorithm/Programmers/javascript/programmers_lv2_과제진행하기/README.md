# 문제

https://school.programmers.co.kr/learn/courses/30/lessons/176962

# 풀이

- 문제에서 제시한 대로 구현만 하면 되는 문제

  1. 시간을 분으로 치환
  2. 과제들을 시작 시간 순으로 오름차순 정렬
  3. 정렬된 과제들을 순회

  - 이전 과제의 완료 예정 시간보다 현재 과제의 시작 시간이 짧으면 -> 이전 과제를 stack에 넣어놓고 새로운 과제를 시작
    - stack에 과제를 추가할 때 `이전 완료 예정 시간 - 현재 작업 시작 시간` 으로 남은 시간 계산
  - 이전 작업 완료 예정 시간과 현재 과제 작업 시간이 같으면 이전 과제를 끝내자마자 새로운 작업을 시작
    - answer에 이전 작업 push
  - 이전 작업 완료 예정 시간이 현재 과제 작업 시간보다 크면 -> 이전 과제를 끝내고 현재 과제를 시작하기까지 공백이 생김
    - 이때 stack에 넣었던 과제들을 수행
    - 공백 시간 blank만큼 stack에 가장 최근 추가한 작업부터 남은 시간 빼기
    - 남은 시간이 공백 시간보다 짧으면 현재 과제를 완료로 pop하고 다음 stack 과제 수행
      - 이때 남은 시간은 직전에 완료한 시간을 빼고 남은 시간으로 갱신

  4.  가장 마지막 과제 완료 후, stack에 넣어둔 과제를 최신 순으로 모두 pop()

- **주의)** stack의 가장 최신 과제 남은 시간을 뺄 때, 공백 시간보다 작거나 같은 경우에 대한 한 번의 조건으로 처리하면 틀린다.(공백 시간이 남아있는한 stack에 넣어둔 과제들을 최대한으로 수행해야 함)

```js
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
```
