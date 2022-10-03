
// 조합
function combinations(arr, r){
  if(r === 1) return arr.map((v) => [v])
  let result = []

  arr.forEach((fixed, idx, arr) => {
    const rest = arr.slice(idx + 1)
    const combis = combinations(rest, r - 1)
    const combine = combis.map((v) => [fixed, ...v])

    result.push(...combine)
  })

  return result
}

// 중복 조합
function combinationsRepeat(arr, r){
  if(r === 1) return arr.map((v) => [v])
  
  let result = []

  arr.forEach((fixed, _, arr) => {
    const combis = combinationsRepeat(arr, r - 1)
    const combine = combis.map((v) => [fixed, ...v])

    result.push(...combine)
  })

  return result
}


const arr = [1,2,3,4,5]
console.log(combinations(arr, 3))
console.log(combinationsRepeat(arr, 3))

