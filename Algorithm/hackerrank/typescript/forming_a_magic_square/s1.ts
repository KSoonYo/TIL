function check(arr: number[][]) {
  const crossLineValue1 = arr[0][0] + arr[1][1] + arr[2][2];
  const crossLineValue2 = arr[0][2] + arr[1][1] + arr[2][0];
  if (crossLineValue1 !== crossLineValue2) {
    return false;
  }

  for (let i = 0; i < 3; i++) {
    let a = 0;
    let b = 0;
    for (let j = 0; j < 3; j++) {
      a += arr[i][j];
      b += arr[j][i];
    }
    if (a !== b || a !== crossLineValue1 || a !== crossLineValue2) {
      return false;
    }
  }

  return true;
}

function getSquare(
  startPos: number[],
  arr: number[][],
  target: Set<number>,
  minV: number[],
  origin: number[][]
) {
  const [r, c] = startPos;
  if (r === 3 && check(arr)) {
    let temp = 0;
    for (let k = 0; k < 3; k++) {
      for (let h = 0; h < 3; h++) {
        temp += Math.abs(origin[k][h] - arr[k][h]);
      }
    }

    minV[0] = Math.min(minV[0], temp);
    return;
  }

  for (let k = 1; k < 10; k++) {
    if (target.has(k)) {
      continue;
    }
    arr[r][c] = k;
    target.add(k);
    if (c === 2) {
      getSquare([r + 1, 0], arr, target, minV, origin);
    } else {
      getSquare([r, c + 1], arr, target, minV, origin);
    }
    arr[r][c] = 0;
    target.delete(k);
  }

  return;
}

function formingMagicSquare(s: number[][]): number {
  // Write your code here
  const arr: number[][] = Array.from(new Array(3), () => Array(3).fill(3));
  const targets = new Set<number>();
  const minV = [9 ** 9];
  getSquare([0, 0], arr, targets, minV, s);
  console.log(minV[0]);
  return minV[0];
}

// formingMagicSquare([
//   [4, 9, 2],
//   [3, 5, 7],
//   [8, 1, 5],
// ]);

formingMagicSquare([
  [4, 5, 8],
  [2, 4, 1],
  [1, 9, 7],
]);
