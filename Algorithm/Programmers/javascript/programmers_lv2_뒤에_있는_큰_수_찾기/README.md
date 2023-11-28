# 문제

정수로 이루어진 배열 numbers가 있습니다. 배열 의 각 원소들에 대해 자신보다 뒤에 있는 숫자 중에서 자신보다 크면서 가장 가까이 있는 수를 뒷 큰수라고 합니다.
정수 배열 numbers가 매개변수로 주어질 때, 모든 원소에 대한 뒷 큰수들을 차례로 담은 배열을 return 하도록 solution 함수를 완성해주세요. 단, 뒷 큰수가 존재하지 않는 원소는 -1을 담습니다.

https://school.programmers.co.kr/learn/courses/30/lessons/154539?language=javascript

## 제한사항

4 ≤ numbers의 길이 ≤ 1,000,000

1 ≤ numbers[i] ≤ 1,000,000

## 입출력 예

| numbers            | result                |
| ------------------ | --------------------- |
| [2, 3, 3, 5]       | [3, 5, 5, -1]         |
| [9, 1, 5, 3, 6, 2] | [-1, 5, 6, 6, -1, -1] |

## 입출력 예 설명

### 입출력 예 #1

2의 뒷 큰수는 3입니다. 첫 번째 3의 뒷 큰수는 5입니다. 두 번째 3 또한 마찬가지입니다. 5는 뒷 큰수가 없으므로 -1입니다.

위 수들을 차례대로 배열에 담으면 [3, 5, 5, -1]이 됩니다.

### 입출력 예 #2

9는 뒷 큰수가 없으므로 -1입니다. 1의 뒷 큰수는 5이며, 5와 3의 뒷 큰수는 6입니다. 6과 2는 뒷 큰수가 없으므로 -1입니다. 위 수들을 차례대로 배열에 담으면 [-1, 5, 6, 6, -1, -1]이 됩니다.

# 풀이

- stack을 이용하는 간단한 문제
- 스택의 가장 마지막에 있는 수보다 새로 들어오는 수가 크면 pop -> 스택의 가장 마지막 수가 새로 들어오는 수보다 클 때까지

```javascript
function solution(numbers) {
  var answer = Array(numbers.length).fill(-1);
  const stack = [];
  let front = 0;
  while (front < numbers.length) {
    const number = numbers[front];
    while (stack.length > 0 && stack.at(-1)[0] < number) {
      answer[stack.at(-1)[1]] = number;
      stack.pop();
    }
    stack.push([number, front]); // [숫자, 현재 위치]
    front++;
  }
  return answer;
}
```
