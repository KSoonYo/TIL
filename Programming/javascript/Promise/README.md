# Promise

- 미래에 비동기 작업이 완료 혹은 실패했을 때 결과의 상태와 결과값을 나타내는 객체

- promise 객체를 사용하면 비동기 작업을 마치 동기 작업처럼 구성하는 것이 가능



## Promise 객체

- 상태
  - pending: 작업이 진행 중
  - fulfiled: 작업 성공
    - `.then` 으로 작업이 성공했을 시 수행할 콜백을 등록할 수 있음
  - rejected: 작업 실패
    - `.catch`로 작업이 실패했을 시 수행할 콜백을 등록할 수 있음

- 작업이 성공하면 성공 결과도 함께 가진다.
- 작업이 실패하면 실패에 대한 이유를 결과로 가진다.

- fetch(), axios() 뿐만 아니라 response 객체의 text() 와 json() 역시 Promise 객체를 반환



### 이중 fetch 함수 실행 시 chaining 방법

```js
fetch(url)
.then((res) => {
	// 첫번째 fetch 함수 성공 시 실행 내용
	
	return fetch(url2) // fetch 함수 요청 후 promise 객체 반환
})
.then((res2) => {
	// 두번째 fetch 함수 성공 시 실행 내용
})
```



## 상황에 따른 then promise 반환 상태

```js
fetch('url')
.then(successCallback, failCallback)
```

- promise가 성공 상태면 .then에서는 첫번째 인자의 callback 함수가 실행된다.
- promise가 실패이면 .then에서 두 번째 인자의 callback 함수가 실행된다.
- promise 객체의 상태가 결정되기만 했다면 언제든지 몇 번이든 then 메소드로 해당 promise 객체와 상태값을 소비할 수 있음
  - 따라서 then 메소드를 반드시 promise의 작업이 완료되기 이전에 미리 작성해야 하는 것이 아님. 작업이 완료되었더라도 상태가 결정된 promise 객체는 이후에 다시 소비하는 것이 가능하기 때문
  - 하단에 `이미 상태가 결정된 promise 객체 만들기` 참조




### 이전 then promise의 콜백 함수가 promise 객체를 반환하는 경우

- then 메소드가 반환하는 promise 객체는 내부 콜백 함수 실행 결과로 반환된 promise 객체의 상태와 결과값을 그대로 갖는다.



### 이전 then promise가 값을 반환하는 경우

- 이전 then이 반환하는 promise 객체가 fullfilled 상태가 되고,  결과값이 다음 then 메소드의 첫번째 callback 함수 인자로 들어온다.



### then 메소드의 callback이 아무 값도 반환하지 않는 경우

- then 메소드가 반환하는 Promise 객체는 fullfilled 상태가 되고 작업 성공 결과로 undefined를 갖게 된다.



### 실행된 콜백 내부에서 에러가 발생했을 때

- then 메소드가 반환하는 promise 객체의 상태는 rejected가 되고 작업 실패 정보로 해당 에러 객체를 갖는다.



### 아무런 콜백이 실행되지 않을 때

- 이전 Promise 객체의 상태와 결과가 다음 체이닝으로 이어진다.





## 직접 Promise 객체 작성

```js
const p = new Promise((resolve, reject) => {	// executor 함수
    
})
```

- Promise 객체 생성 시 executor 실행
  - executor의 인자는 resolve 메소드와 reject 메소드
- resolve 메소드는 Promise 객체 상태를 fullfilled 상태로 만들어준다.
  - 이때 Promise 객체의 결과값을 resolve의 인자로 넣는다.
- reject 메소드는 Promise 객체 상태를 reject 상태로 만들어준다,
  - 이때 reject 메소드의 인자로 Error 객체가 들어간다.(new Error('에러 정보'))



### Promisify

- then 메소드 내부의 callback 함수에서 비동기 실행을 할 때

```js
function wait(text, seconds){
    setTimeout(() => text, 1000 * seconds)
}

fetch('url')
.then((response) => response.text())
.then((result) => wait(result, 3)) // 3초 후에 result 반환
.then((result) => { console.log(result)} )
```

- setTimeout 함수에 등록한 callback 함수는 3초 후에 실행되어 text가 반환되지만, wait 함수 자체는 반환값이 없기 때문에 가장 마지막에 result는 undefined로 출력된다.
  - 따라서 이러한 경우에는 결과값 text를 잇는 chaining이 불가능하다.
- 이때 wait을 promise 객체화 하여 3초 후에 결과값을 반환하는 작업을 다음과 같이 작성 가능

```js
// wait 함수 실행 시 3초 후에 Promise 상태를 fullfill 상태로 전환하는 Promise 객체를 반환  
function wait(text, seconds){
    const p = new Promise((resolve, reject) => {
	    setTimeout(() => {resolve(text)}, 1000 * seconds)    
    })
    return p
}

fetch('url')
.then((response) => response.text())
.then((result) => wait(result, 3)) // 3초 후에 result 텍스트 반환
.then((result) => { console.log(result)} )
```

- wait 함수가 promise 객체를 반환하므로 then 메소드가 반환하는 Promise 객체의 상태와 반환값은 wait 함수가 반환한 Promise 객체와 동일하게 이어진다.

#### 주의점

- 비동기 실행 함수를 동작시킬 때 Promisify는 콜백 헬을 방지할 수 있는 유용한 기법이지만 모든 비동기 실행 함수를 promisify 할 수는 없다.
- setTimeOut이나 readFile과  같이 등록한 콜백을 한 번만 실행하는 경우에만 Promisify 가능
  - setInterval이나 addEventListener와 같은 경우에는 promisify 불가
  - 이유) Promise 객체가 한번 pending 상태에서 fullfilled나 rejected 상태가 되면, 그 뒤로는 그 상태와 결과가 바뀌지 않기 때문이다.
    - resolve 함수가 여러 번 실행되도 해당 Promise 객체가 이미 fullfilled나 rejected라면 상태는 변하지 않고, 이미 resolved되거나 rejected된 결과 또한 변하지 않으므로 .then으로 이어진 경우 chaining이 한 번만 실행된다.





### 이미 상태가 결졍된 Promise 객체 만들기

```js
// rejected 상태의 promise 객체
const p = Promise.reject(new Error('error'))

// fullfilled 상태의 promise 객체
const p = Promise.resolve('success')


// Promise가 fullfilled 상태라면 then의 첫 번째 인자의 콜백 함수가, rejected 상태라면 두 번째 인자의 콜백 함수가 실행된다.
p.then((result) => {console.log(result)}, (error) => {console.log(error)})
```



## 여러 개의 Promise 객체를 배열로 한 번에 처리하기

### all

- [Promise 객체 1, Promise 객체 2 ...] 배열을 인자로 받는 메소드
- 모든 Promise 객체의 상태가 pending에서 fullfilled가 될 때까지 기다리다가 모두 fullfilled가 되면 각 Promise 객체의 성공 결과들로 이루어진 배열을 결과로 가진다.
- Promise 객체 중 하나라도 rejected 상태가 되면 전체 작업이 실패한 것으로 간주되고, all 메소드가 반환되는 promise 객체 또한 rejected 상태가 된 Promise 객체와 동일한 상태와 에러 정보를 가진다.
- all() 메소드의 반환값 또한 Promise 객체이므로 chaining 가능



### race

- all처럼 promise 객체 배열을 인자로 받는다.
- race가 반환하는 Promise 객체는 가장 먼저 fullfilled나 rejected 상태가 된 Promise 객체와 동일한 상태와 결과를 갖는다.



### allSettled 

- 배열 내 모든 Promise 객체가 fullfilled나 rejected 상태가 될 때까지 기다리고, pending 상태의 Promise 객체가 하나도 없으면 allSettled메소드가 반환하는 Promise 객체의 상태값은 fullfilled가 되고 그 작업의 성공 결과로 하나의 배열을 갖는다.

- 배열은 인자로 받았던 각각의 promise 객체 배열의 최종 상태를 나타내는 status 프로퍼티, 작업의 성공 결과는 value 프로퍼티, 작업의 실패 정보는 reasone 프로퍼티로 담은 객체들이 요소로 담긴다.

- ```js
  [
      {status: 'fullfilled', value: 1}, // Promise 객체 1의 결과 정보
      {status: 'fullfilled', value: 2}, // Promise 객체 2의 결과 정보
      {status: 'rejected', reason: Error: an error} // Promise 객체 3의 결과 정보
  ]
  ```



### any

- 여러 promise 객체들 중 가장 먼저 fullfilled가 된 Promise 객체의 상태와 결과가 any가 반환하는 Promise 객체에 똑같이 반영된다.
- 모든 Promise 객체가 rejected라면 any가 반환하는 Promise 객체의 작업 실패 정보로 AggregateError 에러 정보를 갖고 상태는 rejected가 된다.