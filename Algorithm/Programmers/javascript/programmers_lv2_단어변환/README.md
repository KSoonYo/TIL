#문제 설명

두 개의 단어 begin, target과 단어의 집합 words가 있습니다. 아래와 같은 규칙을 이용하여 begin에서 target으로 변환하는 가장 짧은 변환 과정을 찾으려고 합니다.

1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
2. words에 있는 단어로만 변환할 수 있습니다.

예를 들어 `begin`이 "hit", `target`가 "cog", words가 ["hot","dot","dog","lot","log","cog"]라면 `"hit" -> "hot" -> "dot" -> "dog" -> "cog"`와 같이 4단계를 거쳐 변환할 수 있습니다.

두 개의 단어 begin, target과 단어의 집합 words가 매개변수로 주어질 때, 최소 몇 단계의 과정을 거쳐 begin을 target으로 변환할 수 있는지 return 하도록 solution 함수를 작성해주세요.

**제한사항**

각 단어는 알파벳 소문자로만 이루어져 있습니다.

각 단어의 길이는 3 이상 10 이하이며 모든 단어의 길이는 같습니다.

words에는 3개 이상 50개 이하의 단어가 있으며 중복되는 단어는 없습니다.

begin과 target은 같지 않습니다.

변환할 수 없는 경우에는 0를 return 합니다.

## 입출력 예

| begin | target | words                                      | return |
| ----- | ------ | ------------------------------------------ | ------ |
| "hit" | "cog"  | ["hot", "dot", "dog", "lot", "log", "cog"] | 4      |
| "hit" | "cog"  | ["hot", "dot", "dog", "lot", "log"]        | 0      |

## 입출력 예 설명

예제 #1

문제에 나온 예와 같습니다.

예제 #2

target인 "cog"는 words 안에 없기 때문에 변환할 수 없습니다.

---

# 문제 풀이

- BFS 풀이
- 모든 단어의 길이가 같고, 단어의 길이가 3 이상 10이하이므로 큰 부담없이 BFS 탐색 가능
- words의 각 단어의 각 자리에 사용된 알파벳을 기록
  - 2번 조건에 따라 word의 각 자리에 사용된 적이 없는 알파벳은 사용할 필요가 없음
- `[단어, 변경 횟수]`를 원소로 가지는 queue로 bfs 탐색
  - 1번 조건에 따라 각 자리의 알파벳을 하나씩 다른 알파벳으로 변경하고, 변경된 단어가 words에 있는 단어라면 변경횟수를 `+1` 하여 단어와 함께 queue에 enque
  - 이때, 이전에 check한 적이 있는 단어는 굳이 다시 체크할 필요가 없으므로 queue에 추가하지 않는다.

```javascript
function solution(begin, target, words) {
  if (!words.includes(target)) {
    return 0;
  }
  const tableArr = Array.from(new Array(begin.length), () => []);
  const checked = new Set();
  checked.add(begin);

  words.forEach((word) => {
    // word마다 각 위치의 알파벳 철자를 기록
    for (let i = 0; i < word.length; i++) {
      if (tableArr[i].includes(word[i])) {
        continue;
      }
      tableArr[i].push(word[i]);
    }
  });
  const wordsQueue = [[begin, 0]]; // [단어, 카운트 횟수]
  while (wordsQueue.length > 0) {
    const [nowWord, count] = wordsQueue.shift();
    if (nowWord === target) {
      // 현재 단어가 target이라면
      // return count
      return count;
    }
    const nowWordArr = [...nowWord];
    nowWordArr.forEach((char, idx) => {
      tableArr[idx]
        .filter((c) => c !== char) // talbeArr[idx]에서 현재의 철자가 아닌 다른 철자들을 get
        .map((changedChar) => {
          const copiedArr = [...nowWordArr];
          copiedArr[idx] = changedChar; // 해당 자리의 알파벳 변경
          return copiedArr.join("");
        })
        .forEach((changed) => {
          if (words.includes(changed) && !checked.has(changed)) {
            // 변경된 단어가 words에 포함되어 있고, 이전에 한번도 check 한 적이 없다면
            // queue와 checked 에 단어 추가
            wordsQueue.push([changed, count + 1]);
            checked.add(changed);
          }
        });
    });
  }
  return 0;
}
```
