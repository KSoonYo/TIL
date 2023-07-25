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
    for (const order of orders.map((o) => [...o].sort().join(""))) {
      const combines = combinations(Array.from(order), menu);
      for (const comb of combines) {
        const key = comb.join("");
        if (!table.has(key)) {
          table.set(key, 1);
        } else {
          table.set(key, table.get(key) + 1);
        }
      }
    }
    let maxV = Math.max(...table.values());
    for (const [dish, cnt] of table) {
      if (cnt >= 2 && cnt === maxV) {
        answer.push(dish);
      }
    }
  }
  return answer.sort();
}

// best solution
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
