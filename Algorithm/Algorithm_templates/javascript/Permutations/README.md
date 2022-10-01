# 순열

- 예시) [1, 2, 3, 4, 5]
  - n = 5
  - r = 2
  - 5개 중 2개를 `중복없이` 뽑는다. 단, 순서가 다르면 서로 다른 경우
    - 1, 3과 3, 1은 다른 케이스



```js

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



const arr = [1, 2, 3, 4, 5]
console.log(permutations(arr, 3))


```



## 중복 순열

- 예시) [1, 2, 3, 4, 5] 
  - n = 5
  - r = 2
  - {1, 1}, {1, 2}, {1, 3}, {1, 4}, {1, 5}, {2, 1}, {2, 2} ...



```js
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
console.log(permutationsRepeat(arr, 2))

```

