
function solution(numbers) {
  // 문자열 숫자 앞 자리가 큰 순서대로 정렬 방법
  numbers = numbers.map(elem => elem.toString()).sort((a, b) => (b + a) - (a + b))
  return numbers[0] === '0' ? '0' : numbers.join('') 
}