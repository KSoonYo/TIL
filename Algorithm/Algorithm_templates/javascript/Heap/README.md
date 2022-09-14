# Heap

- 기본: 최소힙
  - 힙: 완전 이진 트리의 한 형태
  - 때에 따라 우선순위큐로 구현 가능

- 구현에 따라 최대힙, 최소힙 자유롭게 변경 가능
  - 루트 정점이 최소값을 유지하면 최소힙, 최대값을 유지하면 최대힙



```js
class Heap{
    constructor(){
        this.heap = [null] // 1부터 정점 시작하기 위한 null 초기 원소
    }
    
    /* heap 정점 추가 구현
    	1. heap의 가장 마지막 정점에 값 추가
    	2. 마지막 정점에서 부모 정점과 값을 비교
    	3. 현재 정점이 우선순위가 부모 정점보다 클 경우, 부모 정점과 현재 정점 값을 바꿈
    	4. 현재 정점이 루트 정점까지 도달하거나 부모 정점이 우선순위가 더 높을 때까지  3번 반복
    */
    push(value){
        // 1번
        this.heap.push(value)
        
        // 현재 정점이 루트 정점이라면 정렬이 필요 없으므로 바로 return
        if(this.heap.length === 2){
            return
        }
        
        // 2번 ~ 4번
        let currentIndex = this.heap.length - 1
        let parentIndex = Math.floor(currentIndex / 2)
        while(parentIndex !== 0 || this.heap[parentIndex] > value){
            const temp = this.heap[parentIndex]
            this.heap[parentIndex] = value
            this.heap[currentIndex] = temp
            
            currentIndex = parentIndex
            parentIndex = Math.floor(currentIndex / 2)
        }
    }
    
    /* heap 삭제(추출) 연산
    	1. 루트 정점의 값을 pop
    	2. 가장 마지막 정점을 루트 정점으로 이동
    	3. 현재 정점의 왼쪽 자식 정점과 오른쪽 자식 정점 중 우선순위가 높은 자식 정점을 현재 정점과 우선순위 비교
        4. 자식 정점이 없거나 자식 정점보다 현재 정점이 우선순위가 더 높을 때까지 3번 반복
    */
    pop(){
        // heap이 비어있을 경우 pop 연산 수행 불가
        if(this.heap.length - 1 === 0){
            return null 
        }
        
        // heap에 있는 원소가 1개인 경우 곧바로 pop
        if(this.heap.length - 1 === 1){
            return this.heap.pop()
        }
        
        // 1번 ~ 2번
        const value = this.heap[1]
        this.heap[1] = this.heap.pop()
        
        // 3번 ~ 4번
        let currentIndex = 1
        let leftChildIndex = 2
        let rightChildIndex = 3
        while(
        	this.heap[currentIndex] > this.heap[leftChildIndex] ||
            this.heap[currentIndex] > this.heap[rightChildIndex]
        ){
            // 일반적으로 heap은 왼쪽부터 값이 채워지고 오른쪽부터 값이 사라짐
            // Javascript에서 숫자와 undefined 비교 시 false 반환
            // 따라서 양쪽 자식이 모두 없는 경우에는 while문 조건에 false로 걸림
            // 또한 왼쪽 자식과 오른쪽 자식을 비교할 때 오른쪽 자식의 값의 우선순위가 더 큰 경우를 if 조건으로 먼저 설정하면 오른쪽 자식이 undefined인 경우를 else로 걸러낼 수 있음
            if(this.heap[leftChildIndex] > this.heap[rightChildIndex]){
                const temp = this.heap[currentIndex]
                this.heap[currentIndex] = this.heap[rightChildIndex]
                this.heap[rightChildIndex] = temp
                
               	currentIndex = rightChildIndex
            } else{
                const temp = this.heap[currentIndex]
                this.heap[currentIndex] = this.heap[leftChildIndex]
                this.heap[leftChildIndex] = temp
                
                currentIndex = leftChildIndex
            }
            
            leftChildIndex = currentIndex * 2
            rightChildIndex = currentIndex * 2 + 1
        }
        
        return value
    }
}


const heap = new Heap()
heap.push(3)
heap.push(2)
heap.push(7)
heap.push(1)
console.log(heap) // Heap { heap: [ null, 1, 7, 2, 3 ] }

heap.pop()
console.log(heap) // Heap { heap: [ null, 2, 7, 3 ] }
heap.pop()
console.log(heap) // Heap { heap: [ null, 3, 7 ] }

heap.push(0)
console.log(heap) // Heap { heap: [ null, 0, 7, 3 ] }

```





