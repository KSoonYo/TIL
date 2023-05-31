function solution(numbers) {
    var answer = Array(numbers.length).fill(-1);
    const stack = [];
    let front = 0;
    while(front < numbers.length){
        const number = numbers[front];
        while(stack.length > 0 && stack.at(-1)[0] < number){
            answer[stack.at(-1)[1]] = number;
            stack.pop();         
        }
        stack.push([number, front])         // [숫자, 현재 위치]
        front++;
    }
    return answer;
}