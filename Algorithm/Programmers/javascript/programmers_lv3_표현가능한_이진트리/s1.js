function check(bits, root, status = 1) {
  // leaf node라면
  if (bits.length === 1) {
    // 이전 root node가 0이고 현재 노드가 1이라면
    // 표현 불가능한 이진트리
    if (status === 0 && bits[root] === "1") {
      return 0;
    }
    // 그 외는 모두 가능
    return 1;
  }
  // 이전 root 노드가 0인데 현재 노드는 1이라면 더 재귀하지 않고 return 0
  if (status === 0 && bits[root] === "1") {
    return 0;
  }

  let left = bits.slice(0, root);
  let right = bits.slice(root + 1);

  let leftChecked = check(
    left,
    Math.floor(left.length / 2),
    parseInt(bits[root])
  );
  let rightChecked = check(
    right,
    Math.floor(right.length / 2),
    parseInt(bits[root])
  );
  if (leftChecked === 0 || rightChecked === 0) {
    return 0;
  }
  return 1;
}

function solution(numbers) {
  var answer = [];
  // 10진수 -> 2진수 변환(앞에 '0'붙이기: 중위 순회 + 문제 조건에 따라 root 노드는 항상 가운데 있어야 하고, 전체 노드는 포화 이진 트리이므로 2 ** n - 1 개수만큼 있어야 한다.)
  // ** 더미노드는 나중에 추가된 노드이므로 leaf 노드가 있음에도 부모가 더미인 경우는 발생해서는 안된다. **
  // 노드가 1인 경우도 이진트리

  numbers.forEach((number) => {
    let bits = number.toString(2);
    let n = 0;
    while (2 ** n - 1 < bits.length) {
      n++;
    }
    bits = "0".repeat(2 ** n - 1 - bits.length) + bits;
    let root = Math.floor(bits.length / 2);
    let result = check(bits, root, parseInt(bits[root]));
    answer.push(result);
  });
  return answer;
}
