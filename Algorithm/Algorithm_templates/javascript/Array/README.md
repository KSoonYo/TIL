# Array 

## 문자열을 Array로 변환

```js
const string = 'abcdefg'

const toArray = [...string]
console.log(toArray)

/**
output
[
  'a', 'b', 'c',
  'd', 'e', 'f',
  'g'
]
*/
```

### Array를 문자열로 변환

```js
const array = ['a', 'b', 'c']
const toString = array.join('')

console.log(toString) // output: abc
```



## 2차원 배열 만들기

- 0으로 채워진 4 x 3 행렬, false로 채워진 4x3 행렬

```js
const [r, c] = [4, 3]
const board = Array.from(new Array(r), () => Array(c).fill(0))
const board2 = Array.from(new Array(r), () => Array(c).fill(false))

console.log(board) // [ [ 0, 0, 0 ], [ 0, 0, 0 ], [ 0, 0, 0 ], [ 0, 0, 0 ] ]
console.log(board2)
/*
[
  [ false, false, false ],
  [ false, false, false ],
  [ false, false, false ],
  [ false, false, false ]
]
*/
```



## 3차원 배열 만들기

- 주어진 그래프에서 0으로 채워진 x=4, y=3, z=3  방문 배열

```js
const visit = [0, 0, 0, 0].map(elem => Array.from(new Array(3), () => Array(3).fill(0)))

console.log(visit)

/*
[
  [ [ 0, 0, 0 ], [ 0, 0, 0 ], [ 0, 0, 0 ] ],
  [ [ 0, 0, 0 ], [ 0, 0, 0 ], [ 0, 0, 0 ] ],
  [ [ 0, 0, 0 ], [ 0, 0, 0 ], [ 0, 0, 0 ] ],
  [ [ 0, 0, 0 ], [ 0, 0, 0 ], [ 0, 0, 0 ] ]
]
*/
```



## 배열 내 요소 정렬

- sort() 사용
  - 내부 콜백함수의 인자로 a, b의 값이 들어간다.
    - 오름차순 정렬 시
      - a < b이면, 즉 반환값이 a - b < 0 이면 a는 b의 앞에 위치한다.
      - a = b이면, 즉 반환값이 a - b = 0 이면 a 와 b는 순서를 바꾸지 않는다.
      - a > b 이면, 즉 반환값이 a - b > 0 이면 b가 a의 앞에 위치한다.
      - 반환값의 부호를 반대로 하면 내림차순, 오름차순 정렬 전환이 가능하다.

```js
const arr = [1000, 26, 3233, 5]

// 오름차순
arr.sort((a, b) => {
    if(a < b){
        return -1
    } else if(a === b){
        return 0
    } else if(a > b){
        return 1
    }
})

console.log(arr) // [ 5, 26, 1000, 3233 ]

// 내림차순
arr.sort((a, b) => {
    if(a < b){
        return 1
    } else if(a === b){
        return 0
    } else if(a > b){
        return -1
    }
})

console.log(arr) // [ 3233, 1000, 26, 5 ]

// 오름차순 축약형
arr.sort((a, b) => {
    return a - b
})

// 내림차순 축약형
arr.sort((a, b) => {
    return b - a
})

console.log(arr)
```



## 배열 내 문자열 숫자 정렬

- 기본적으로 js에서 sort() 는 배열 요소 내에 숫자를 문자열로 변환하여 정렬

- `'1', '10', '3', '6', '52' '100'` 의 경우,
  - 예를 들어 내림차순의 경우에는`'100', '10', '1', '3', '52', '6'`으로 정렬되어야 함

```js
const numbers = ['1', '10', '3', '6', '52' '100']

numbers.sort()			// 오름차순
numbers.sort((a, b) => (a + b) - (b + a)) // 오름차순
numbers.sort((a, b) => (b + a) - (a + b)) // 내림차순

```



## 배열 내 문자 사전 순 정렬

- sort() 자체 기능으로 오름차순 사전 순 정렬 가능

- String일 때는 `-` 를 이용한 축약형으로 정렬 불가

```js
const words = ['banana', 'apple', 'dagree', 'cold']
// 오름차순(사전순)
words.sort()

// 내림차순 정렬 방법 1
words.sort()
words.reverse()

// 내림차순 정렬 방법 2
words.sort((a, b) => {
    if(a > b) return -1
    else if(b > a) return 1
    else return 0
})

```

