class Heap{
  constructor(){
      this.heap = [null] 
  }
  

  push(value){
      this.heap.push(value)
      
      if(this.heap.length === 2){
          return
      }
      
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
  
 
  pop(){
      if(this.heap.length - 1 === 0){
          return null 
      }
      
      if(this.heap.length - 1 === 1){
          return this.heap.pop()
      }
      
      const value = this.heap[1]
      this.heap[1] = this.heap.pop()
      
      let currentIndex = 1
      let leftChildIndex = 2
      let rightChildIndex = 3
      while(
        this.heap[currentIndex] > this.heap[leftChildIndex] ||
          this.heap[currentIndex] > this.heap[rightChildIndex]
      ){
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


