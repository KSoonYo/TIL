// 문자열을 Array로 변환
const string = 'abcdefg'

const toArray = [...string]
console.log(toArray)


// Array를 문자열로 변환
const array = ['a', 'b', 'c']
const toString = array.join('')

console.log(toString)


// 2차원 배열 만들기
const [r, c] = [4, 3]
const board = Array.from(new Array(r), () => Array(c).fill(0))
const board2 = Array.from(new Array(r), () => Array(c).fill(false))

console.log(board)  
console.log(board2)



// 3차원 배열 만들기
const visit = [0, 0, 0, 0].map(elem => Array.from(new Array(3), () => Array(3).fill(0)))
console.log(visit)


// 배열 내 요소 정렬
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

// 문자열 숫자 정렬
const numbers = ['1', '10', '3', '6', '52', '100']
numbers.sort() // 오름차순
numbers.sort((a, b) => (a + b) - (b + a)) // 오름차순
numbers.sort((a, b) => (b + a) - (a + b)) // 내림차순
console.log(numbers)


// 문자열 사전 순 정렬
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

console.log(words)

