# 조합

- 예시: [1, 2, 3, 4, 5]
  - n = 5
  - r = 3
  - {1, 2}, {1, 3}, {1, 4}, {1, 5}, {2, 3} ... ...

```js
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

const arr = [1,2,3,4,5]
console.log(combinations(arr, 3))
```





## 중복 조합

- 요소 n 개 중 r개를 중복을 허용하며 뽑는 조합
- [1, 2, 3, 4, 5]
  - n = 5
  - r = 3
  - {1, 1, 1}, {1, 1, 2}, {1, 1, 3}, {1, 1, 4}, {1, 1, 5} ...

```js
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
console.log(combinationsRepeat(arr, 3))
```

