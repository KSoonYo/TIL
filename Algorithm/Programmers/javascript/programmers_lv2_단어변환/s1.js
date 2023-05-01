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
