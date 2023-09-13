# this

- 자신이 속한 객체 또는 자신이 생성할 인스턴스를 가리키는 자기 참조 변수다.
- this를 통해 자신이 속한 객체 또는 생성할 인스턴스의 프로퍼티나 메서드를 참조할 수 있다.

  ```js
  // 객체
  const obj = {
    value: 8,
    printValue() {
      return this.value; // this는 obj 객체를 가리킨다.
    },
  };

  console.log(obj.printValue()); // 8

  // 생성자 함수
  const F = function (value) {
    this.value = value;
  };

  F.prototype.getValue = function () {
    return this.value; // this는 생성자 함수 F의 인스턴스를 가리킨다.
  };

  const instance1 = new F(3);
  instance1.getValue(); // 3 출력

  const instance2 = new F(5);
  instance2.getValue(); // 5 출력
  ```

- this는 자바스크립트 엔진을 통해 암묵적으로 생성되며, 코드 어디서든 참조할 수 있다.
- 함수를 호출하면, arguments 객체와 this가 암묵적으로 함수 내부에 전달된다. 또한 지역변수처럼 사용 가능하다.
- strict 모드도 this 바인딩에 영향을 준다.
- 단, this가 가리키는 값. 즉, **this 바인딩은 함수 호출 방식에 의해 동적으로 결정된다.**

**바인딩** : 식별자와 값을 연결하는 과정

- 변수 바인딩: 변수 이름(식별자)과 확보된 메모리 공간 주소를 바인딩
- this 바인딩: this 키워드(식별자 역할을 하는 키워드)와 this가 가리키길 객체를 바인딩

---

## 함수 호출 방식에 따른 this 바인딩

1. 일반 함수 호출
2. 메서드 함수 호출
3. 생성자 함수 호출
4. Function.prototype.apply/call/bind 메서드에 의한 간접 호출

```js
const foo = function () {
  console.dir(this);
};

// 1. 일반 함수 호출
foo(); // window

// 2. 메서드 호출
const obj = { foo };
obj.foo(); // obj

//3. 생성자 함수 호출
new foo(); // foo{}

//4. Function.prototype.apply/call/bind 메서드에 의한 간접 호출
const bar = { name: "bar" };
foo.call(bar); // bar
foo.apply(bar); // bar
foo.bind(bar)(); // bar
```

### 일반 함수 호출

- 기본적으로 this는 전역 객체가 바인딩 된다.
- 전역함수는 물론, 중첩 함수를 일반함수로 호출하면 함수 내부의 this는 모두 전역 객체가 바인딩

```js
function foo() {
  console.log("foo's this:", this);
  function bar() {
    console.log("bar's this:", this);
  }
  bar(); // window
}
foo(); // window
```

```js
var value = 10;
const example = {
  value: 100,
  method() {
    console.log(this); // example 객체 {value: 100, method: f}
    console.log(this.value); // 100
    function inner() {
      console.log(this); // window
      console.log(this.value); // 10
    }
    setTimeout(function () {
      console.log(this); // window
      console.log(this.value); // 10
    }, 100);
    inner();
  },
};

example.method();
```

- 콜백 함수가 **일반 함수로 호출되면** 콜백 함수 내부의 this에도 전역 객체가 바인딩된다.

```js
var value = 1;
const obj = {
  value: 100,
  foo() {
    const that = this;
    setTimeout(
      function () {
        console.log(that.value); // 1번, 100 출력
        console.log(this.value); // 2번, 100 출력
      }.bind(this),
      100
    );
    // 아니면 화살표 함수를 사용하는 방법도 있다.
    setTimeout(() => console.log(this.value), 100);
  },
};
```

- 추가) strict 모드에서는 undefined가 바인딩된다.
  - class 내부 메소드는 기본적으로 strict 모드이므로, class 내부 메서드에서의 전역 객체 this 바인딩은 `undefined`가 된다.

### 메서드 호출

- 메서드 내부의 `this`에는 메서드를 호출한 객체, 즉 메서드를 호출할 때, 연산자 앞에 붙은 객체가 바인딩 된다.
- 메서드는 **객체에 포함된 것이 아니라, 독립적으로 존재하는 별도의 객체**다.
- 따라서, getName 프로퍼티가 가리티는 함수객체인 getName 메서드는 할당이 가능하다.
  - 다른 객체의 프로퍼티에 할당하는 것으로 다른 객체의 메서드가 될 수도 있다.
  - 일반 변수에 할당하여 일반 함수로 호출될 수도 있다.
- 이 함수 객체는 함수 호출시에 어떤 객체에 this가 바인딩 될 것인지 정한다.

```js
const person = {
  name: "Lee",
  getName() {
    return this.name;
  },
};

const me = {
  name: "Shin",
};
me.getName = person.getName; // 다른 객체의 메서드에 할당 가능
console.log(me.getName()); // "Shin" 출력

const getName = person.getName;
console.log(getName()); // 일반 함수로 호출했으므로 전역객체가 this에 바인딩됨. -> window.name
```

### 생성자 함수 호출

- 생성자 함수의 내부에 있는 this는 생성자 함수의 인스턴스가 바인딩된다.

```js
function Circle(radius) {
  this.radius = radius;
  this.getDiameter = function () {
    return 2 * this.radius;
  };
}

const circle1 = new Circle(5); // -> circle이 this에 바인딩 된다.
console.log(circle1.getDiameter(), circle1.radius); // -> 10, 5

const circle2 = Circle(10); // -> 일반함수로 호출했으니 전역객체가 this에 바인딩 된다.
console.log(circle2); // -> Circle에 return 문이 없으므로 undefined
console.log(getDiameter(), radius); // -> 20 10, 전역 객체의 파라미터이므로 가능
```

### Function.prototype.apply/call/bind 메서드에 의한 간접 호출

- apply

```js
func.apply(thisArg, [argsArray]);
```

- 함수 func을 호출할 때 `thisArg` 객체를 this 인자로 받고, 그 외 함수 인자를 **`배열`**로 전달

  ```js
  function getThisBinding(args1, args2, args3) {
    console.log(args1, args2, args3); // 1 2 3
    return this;
  }
  const thisArg = { a: 1 };
  console.log(getThisBinding.apply(thisArg, [1, 2, 3])); // {a: 1}
  ```

- call

```js
func.call(thisArg[, arg1[, arg2[, ...]]])
```

- 함수 func을 호출할 때 `thisArg` 객체를 this 인자로 받고, 그 외 함수 인자들을 `쉼표(,)` 로 구분해서 전달

  ```js
  function getThisBinding(args1, args2, args3) {
    console.log(args1, args2, args3); // 1 2 3
    return this;
  }
  const thisArg = { a: 1 };
  console.log(getThisBinding.call(thisArg, 1, 2, 3)); // {a: 1}
  ```

- bind

```js
  func.bind(thisArg[, arg1[, arg2[, ...]]])
```

- 함수 func에 thisArg를 this로 바인딩하고 인자를 쉼표로 구분하여 전달
  - 함수를 호출할 때 this 인자가 아닌 나머지 인자를 넘겨주는 방식도 가능
- 명시적으로 호출한 것은 아니기 때문에 bind한 후에 호출을 해줘야 함수가 실행된다.
  ```js
  function getThisBinding(args1, args2, args3) {
    console.log(args1, args2, args3); // 1, 2, 3
    return this;
  }
  const thisArg = { a: 1 };
  console.log(getThisBinding.bind(thisArg, 1, 2, 3)()); // {a : 1}
  console.log(getThisBinding.bind(thisArg)(1, 2, 3)); // {a : 1}
  ```
