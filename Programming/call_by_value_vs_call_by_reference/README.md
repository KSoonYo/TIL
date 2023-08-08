# Call by value vs Call by reference

## TL;DR

- Call by value
  - 함수를 호출할 때 값을 복사하여 인자로 넘기는 방식
- Call by reference
  - 함수를 호출할 때 참조를 전달하는 방식

---

## Call by value

- 함수 호출 시, 값을 `복사` 하여 인자로 넘겨서 호출
- 함수 내부에서 전달된 변수를 변경해도 외부에 영향을 끼치지 않음

```c
#include<stdio.h>

void func(int a) {
  printf("before in func: %d\n", a);
  a = 300;
  printf("after in func: %d\n", a);
}
int main(void) {
 int a = 100;
 printf("before in main: %d\n", a); // a = 100
 func(a); // func의 매개변수 a에 main의 지역변수 a의 값인 100을 복사하여 전달
 printf("after in main: %d\n", a);
return 0;
}
```

```shell
# output
before in main: 100
before in func: 100
after in func: 300
after in main: 100
```

- 위 예시에서 main 내 지역변수 a와 func의 매개변수 a는 이름만 같은 별개의 변수
  - `func`의 매개변수 a에 `main`의 지역변수 a의 값인 100을 복사하여 전달
- 별도의 메모리 공간에서 값을 보유

## Call by reference

- 함수 호출 시, 변수의 참조값(주소값)을 그대로 매개변수에 전달하는 방식
- 함수 내부에서 주소값을 변경하거나 해당 주소가 참조하고 있는 값을 변경하면 외부 변수에도 영향을 끼침

```c
#include <stdio.h>

void func(int *c, int *d) {
  printf("before in func: c pointing at %p | d pointing at %p\n", c, d);
  printf("before in func: c value: %d | d value: %d\n", *c, *d);
  *c = *c * 10;
  *d = *d * 10;

  printf("after in func: c pointing at %p | d pointing at %p\n", c, d);
  printf("after in func: c value: %d | d value: %d\n", *c, *d);
}

int main(void) {
  int va = 100;
  int vb = 200;
  int *a = &va;  // va의 주소값을 pointer a가 참조
  int *b = &vb;  // vb의 주소값을 pointer b가 참조

  printf("before in main: a pointing at %p | b pointing at %p\n", a, b);
  printf("before in main: a value: %d | b value: %d\n", *a, *b);
  func(a, b);
  printf("after in main: a pointing at %p | b pointing at %p\n", a, b);
  printf("after in main: a value: %d | b value: %d\n", *a, *b);

  return 0;
}
```

```shell
before in main: a pointing at 0x7ffd1c57b45c | b pointing at 0x7ffd1c57b458
before in main: a value: 100 | b value: 200
before in func: c pointing at 0x7ffd1c57b45c | d pointing at 0x7ffd1c57b458
before in func: c value: 100 | d value: 200
after in func: c pointing at 0x7ffd1c57b45c | d pointing at 0x7ffd1c57b458
after in func: c value: 1000 | d value: 2000
after in main: a pointing at 0x7ffd1c57b45c | b pointing at 0x7ffd1c57b458
after in main: a value: 1000 | b value: 2000
```

- `pointer a`와 `pointer b` 가 참조하고 있는 주소 : `0x7ffd1c57b45c`, `0x7ffd1c57b458`
  - a가 참조하고 있는 주소가 저장하고 있는 값: 100
  - b가 참조하고 있는 주소가 저장하고 있는 값: 200
- `pointer c` 와 `pointer d` 는 pointer a와 pointer b의 주소값을 그대로 가짐
  - `pointer c` 와 `pointer d` 에서 가리키고 있는 주소가 저장하고 있는 값에 \*10
  - 각각의 주소에 저장하고 있는 값이 1000과 2000으로 변경됨
- `pointer a`와 `pointer b`도 같은 주소를 참조하고 있으므로 해당 주소에 저장된 값인 1000과 2000을 그대로 참조
- 매개변수로 전달된 참조값으로 값을 변경하여 외부 변수가 참조하고 있는 값 또한 변경되었으므로 `call by reference`

### Is It Real?

아래와 같이 func 함수 내부에 임시 변수 temp를 선언하여 c의 주소값을 변경

```c
#include <stdio.h>

void func(int *c, int *d) {
  printf("before in func: c pointing at %p | d pointing at %p\n", c, d);
  printf("before in func: c value: %d | d value: %d\n", *c, *d);
  ////////////////// 추가
  int temp = 0;
  c = &temp;
  //////////////////
  *c = *c * 10;
  *d = *d * 10;

  printf("after in func: c pointing at %p | d pointing at %p\n", c, d);
  printf("after in func: c value: %d | d value: %d\n", *c, *d);
}

int main(void) {
  int va = 100;
  int vb = 200;
  int *a = &va;
  int *b = &vb;
  printf("before in main: a pointing at %p | b pointing at %p\n", a, b);
  printf("before in main: a value: %d | b value: %d\n", *a, *b);
  func(a, b);
  printf("after in main: a pointing at %p | b pointing at %p\n", a, b);
  printf("after in main: a value: %d | b value: %d\n", *a, *b);

  return 0;
}
```

```shell
before in main: a pointing at 0x7ffc450dab58 | b pointing at 0x7ffc450dab54
before in main: a value: 100 | b value: 200
before in func: c pointing at 0x7ffc450dab58 | d pointing at 0x7ffc450dab54
before in func: c value: 100 | d value: 200
after in func: c pointing at 0x7ffc450dab5c | d pointing at 0x7ffc450dab54
after in func: c value: 0 | d value: 2000
after in main: a pointing at 0x7ffc450dab58 | b pointing at 0x7ffc450dab54
after in main: a value: 100 | b value: 2000
```

- c가 참조하고 있는 주소값이 `0x7ffc450dab58` 에서 `0x7ffc450dab5c` 으로 변경되었고, c가 참조하고 있는 주소에 저장된 값 또한 0으로 출력
- 하지만 func 함수 외부에서 전달한 `pointer a가 가리키는 주소값`은 변경되지 않음
- 다시 말해서 pointer c와 d는 pointer a와 b가 가리키는 주소값을 **`복사`** 하여 해당 주소를 가리킨다는 것을 알 수 있음
- 주소값을 복사하고, 주소값의 변경이 외부 변수에 영향을 끼치지 않는다는 점에서 위 예시는 `call by value` 로 볼 수 있음

  - 일부에서는 이런 전달 방식을 `call by address` 라고 부르기도 함

- Java에서는 메모리 주소를 참조하는 자료형의 경우, 이와 비슷한 방식으로 함수 매개 변수에 참조 타입 변수의 참조 주소값을 복사하여 전달

  - 관점에 따라 동일한 주소 참조를 전달하여 값의 변경이 함수 외부에도 영향을 끼치므로 사용자 입장에서는 `call by reference` 라고 해도 무방하다는 입장과 Java는 메모리 주소에 직접 접근하는 방법을 막고 있기 때문에 사용자가 직접 참조를 통한 값의 변경이 애초에 불가능하고 내부 동작상 **객체의 주소값을 매개변수에 복사**하여 사용하기 때문에 Java는 `call by value` 만 있다고 하는 입장으로 갈린다.
    - 다만 Java 내부 동작상 `call by value`로 보는 것이 더 정확하다.
  - Java 창시자 제임스 고슬링은 `pass by value`(call by value)만 참고했다고 밝혔다.

  ```plain
  the Java authors choose to only include one simple idea - pass-by-value, with no default values or optional parameter (overloading often provides a satisfactory alternative), no variable length parameter lists (added finally in Java 5), no named parameters, no pass-by-reference, no const (a general Java issue) parameters, etc.

  -The Java Programming Language, 2nd ed. by Ken Arnold and James Gosling, section 2.6.1, page 40, 3rd paragraph.

  ```

## References

https://stackoverflow.com/questions/40480/is-java-pass-by-reference-or-pass-by-value

https://www.baeldung.com/java-pass-by-value-or-pass-by-reference
