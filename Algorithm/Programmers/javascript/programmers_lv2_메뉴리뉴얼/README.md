# 문제

https://school.programmers.co.kr/learn/courses/30/lessons/72411

# 풀이

- 나의 풀이)

  - 코스 요리 길이에 따라 orders 배열의 각 주문에서 요리 단품으로 만들 수 있는 모든 조합을 구한 뒤에 table로 count
  - 주의점) 'XY' 와 'YX'는 같은 개수로 카운트되어야 하므로 주문 별 요리는 모두 사전 순으로 정렬된 이후에 조합을 구해야 함

  ```js
  function combinations(arr, r) {
    if (r === 1) return arr.map((v) => [v]);

    const result = [];
    arr.forEach((fixed, idx, arr) => {
      const rest = arr.slice(idx + 1);
      const comb = combinations(rest, r - 1);
      const combine = comb.map((v) => [fixed, ...v]);
      result.push(...combine);
    });

    return result;
  }

  function solution(orders, course) {
    var answer = [];
    for (const menu of course) {
      const table = new Map();
      for (const order of orders.map((o) => o.split("").sort().join(""))) {
        // 주문 별 menu 길이 만큼의 가능한 조합
        const combines = combinations(Array.from(order), menu);

        // count
        for (const comb of combines) {
          const key = comb.join("");
          if (!table.has(key)) {
            table.set(key, 1);
          } else {
            table.set(key, table.get(key) + 1);
          }
        }
      }

      // 주문량이 가장 많은 메뉴
      let maxV = Math.max(...table.values());
      for (const [dish, cnt] of table) {
        if (cnt >= 2 && cnt === maxV) {
          answer.push(dish);
        }
      }
    }
    return answer.sort();
  }
  ```

- best solution)

  - 기본 컨셉은 동일하나 코드가 더 간결
  - 주문 음식을 사전 순으로 정렬하고, course 길이만큼 dfs로 가능한 조합을 구한다.
  - 이후 배열로 해당 course 길이 만큼의 maxNum을 갱신 + candidates(코스 후보군) 테이블에도 기록

  ```js
  function solution(orders, course) {
    const ordered = {};
    const candidates = {};
    const maxNum = Array(10 + 1).fill(0);
    const createSet = (arr, start, len, foods) => {
      if (len === 0) {
        ordered[foods] = (ordered[foods] || 0) + 1;
        if (ordered[foods] > 1) candidates[foods] = ordered[foods];
        maxNum[foods.length] = Math.max(maxNum[foods.length], ordered[foods]);
        return;
      }

      for (let i = start; i < arr.length; i++) {
        createSet(arr, i + 1, len - 1, foods + arr[i]);
      }
    };

    orders.forEach((od) => {
      // arr.sort는 기본적으로 사전식 배열
      const sorted = od.split("").sort();
      // 주문한 음식을 사전순으로 배열해서 문자열을 만든다.
      // course에 있는 길이만 만들면 된다.
      course.forEach((len) => {
        createSet(sorted, 0, len, "");
      });
    });

    const launched = Object.keys(candidates).filter(
      (food) => maxNum[food.length] === candidates[food]
    );

    return launched.sort();
  }
  ```
