
// 순열: n!
function permutations(arr, n){
  if(n === 1){
    return arr.map((v) => [v])
  }
  let result = []

  arr.forEach((fixed, idx, arr) => {
    const rest = arr.filter((_, index) => index !== idx)
    const perms = permutations(rest, n - 1)
    const combine = perms.map((v) => [fixed, ...v])
    result.push(...combine)
  })
  return result
}

// 중복순열: n ^ r
function permutationsRepeat(arr, n){
  if(n == 1){
    return arr.map((v) => [v])
  }

  let result = []
  arr.forEach((fixed, _, arr) => {
    const perms = permutationsRepeat(arr, n - 1)
    const combine = perms.map((v) => [fixed, ...v])
    result.push(...combine)
  })
  return result
}

const arr = [1, 2, 3, 4, 5]
console.log(permutations(arr, 2))
console.log(permutationsRepeat(arr, 2))
