# Queue

- FIFO(선입선출)
- Array 구현 방법, Linked List 구현 방법



## Array를 이용한 구현

- 배열의 크기, front, rear가 무한정 늘어날 우려가 있음

```js
class Queue {
  constructor(value){
      this.queue = []
      this.front = 0
      this.rear = 0
  }
  
  enqueue(value){
      this.queue[this.rear++] = value
  }
  
  dequeue(){
      const v = this.queue[this.front]
      delete this.queue[this.front]
      this.front += 1
      return v
  }
  
  isPrinted(p){
      return this.queue.filter((elem) => elem.length > 0 && elem[0] > p).length === 0
  }
  
  isEmpty(){
      return this.front === this.rear
  }
}

```



## Linked List를 이용한 구현

- Node 객체 구현

- enqueue, dequeue, peek

```js
class Node{
  constructor(value){
    this.value = value;
    this.next = null;
  }
}

class Queue{
  constructor(){
    this.head = null;
    this.tail = null
  }

  enqueue(value){
    const newNode = new Node(value)
    if(this.head === null){
      this.head = this.tail = newNode;
    } else{
      this.tail.next = newNode;
      this.tail = newNode;
    }
  }

  dequeue(){
    const value = this.head.value;
    this.head = this.head.next;
    return value
  }

  peek(){
    return this.head.value
  }
}


function solution(priorities, location) {
  const q =  new Queue();

  for(let i = 0; i < priorities.length; i += 1){
    q.enqueue([priorities[i], i])
  }

  priorities.sort((a, b) => b - a)

  let count = 0;
  while(true){
    const currentValue = q.peek();
    if(currentValue[0] < priorities[count]){
      q.enqueue(q.dequeue())
    } else{
      const value = q.dequeue();
      count += 1
      if(location === value[1]){
        return count
      }
    }
  }
}

```

