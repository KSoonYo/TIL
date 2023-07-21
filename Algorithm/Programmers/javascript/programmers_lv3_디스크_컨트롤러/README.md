# 문제

https://school.programmers.co.kr/learn/courses/30/lessons/42627?language=javascript

# 풀이

- 핵심) 가장 빨리 요청된 작업들 중 소요 시간이 짧은 작업을 먼저 실행

  - timer를 1초씩 돌리면서 현재 시간에 요청된 작업들을 disks에 추가
    - disks는 소요 시간이 짧은 작업을 정렬해주는 최소 heap
  - time이 이전에 실행했던 작업의 완료 시간 이상이 되면 새로운 작업을 disks에서 pop해서 작업의 완료 시간 갱신
    - 개별 작업 별로 `(최종 완료 시간 - 해당 작업의 요청 시간)`을 하여 작업 별로 요청 부터 작업 완료까지 걸린 시간을 count
  - 작업 별 작업 완료 시간을 모두 더해서 작업의 개수를 나누면 평균을 구할 수 있음

- Heap을 쓰지 않고 정렬로 푸는 방법도 있지만 시간복잡도가 더 오래 걸린다.
- 참고) SJF 알고리즘

```js
class Heap {
  constructor() {
    this.heap = [null];
  }

  length() {
    return this.heap.length - 1;
  }

  push(item) {
    // 마지막에 원소 추가
    this.heap.push(item);
    let idx = this.heap.length - 1;
    let parent = Math.floor(idx / 2);

    // 부모 정점과 우선 순위 비교
    while (idx > 1 && this.heap[parent][1] > this.heap[idx][1]) {
      const node = this.heap[parent];
      this.heap[parent] = this.heap[idx];
      this.heap[idx] = node;
      idx = parent;
      parent = Math.floor(idx / 2);
    }
  }

  pop() {
    const min = this.heap[1];
    if (this.heap.length <= 2) this.heap = [null];
    else this.heap[1] = this.heap.pop();

    let curIdx = 1;
    let leftIdx = curIdx * 2;
    let rightIdx = curIdx * 2 + 1;

    if (!this.heap[leftIdx]) return min;
    if (!this.heap[rightIdx]) {
      if (this.heap[leftIdx][1] < this.heap[curIdx][1]) {
        [this.heap[leftIdx], this.heap[curIdx]] = [
          this.heap[curIdx],
          this.heap[leftIdx],
        ];
      }
      return min;
    }

    while (
      this.heap[leftIdx][1] < this.heap[curIdx][1] ||
      this.heap[rightIdx][1] < this.heap[curIdx][1]
    ) {
      const minIdx =
        this.heap[leftIdx][1] > this.heap[rightIdx][1] ? rightIdx : leftIdx;
      [this.heap[minIdx], this.heap[curIdx]] = [
        this.heap[curIdx],
        this.heap[minIdx],
      ];
      curIdx = minIdx;
      leftIdx = curIdx * 2;
      rightIdx = curIdx * 2 + 1;

      if (leftIdx >= this.heap.length - 1) break;
    }

    return min;
  }
}

function solution(jobs) {
  var answer = 0;

  // 소요 시간이 짧은 순으로 한 번에 정렬 -> 문제점) 앞 작업이 끝난 후 뒤 작업의 요청 시간까지 공백이 발생할 수 있음
  // 빨리 들어온 작업 수행 중에 작업 소요 시간이 짧은 작업을 우선으로 처리하기 -> 최소힙 구현
  const N = jobs.length;

  // 요청 시간 순으로 오름차순 정렬하고, 같은 요청 시간에 대해서는 소요시간이 짧은 순으로 정렬
  const tasks = jobs.sort(([a, b], [c, d]) => a - c || b - d);

  const disks = new Heap();

  let time = 0;
  let complete = 0;
  let total = 0;

  while (tasks.length || disks.length()) {
    while (tasks.length) {
      if (tasks[0][0] === time) {
        disks.push(tasks.shift());
      } else break;
    }

    if (disks.length() && time >= complete) {
      const task = disks.pop();
      complete = task[1] + time;
      total += complete - task[0];
    }
    time++;
  }

  return Math.floor(total / N);
}

// best solution
function solution(jobs) {
  jobs.sort(([a, b], [c, d]) => a - c || b - d);
  const waiting = [];
  const count = jobs.length;
  let processed_time = 0;
  let time = 0;
  while (jobs.length + waiting.length) {
    let in_process;
    while (jobs.length && jobs[0][0] <= time) {
      waiting.push(jobs[0] && jobs.shift());
    }
    if (waiting.length) {
      in_process = waiting.sort(([a, b], [c, d]) => b - d || a - c).shift();
    } else {
      in_process = jobs.shift();
      time = in_process[0];
    }
    time += in_process[1];
    processed_time += time - in_process[0];
  }
  return Math.floor(processed_time / count);
}
```
