# Promise로 타임아웃을 구현하는 code snippet

- `Promise.race` 활용

```javascript
const TIMEOUT_DURATION = 5000; // 타임아웃 시간 (5초)

const apiCall = async () => {
  const PromiseA = await fetch("url", {});
  const timer = new Promise((_, reject) => {
    setTimeout(
      () => reject(new Error("요청 시간이 초과되었습니다.")),
      TIMEOUT_DURATION
    );
  });

  try {
    return await Promise.race([PromiseA, timer]);
  } catch (e) {
    throw new Error(JSON.stringfy(e));
  }
};

apiCall();
```

**참고**

https://www.youtube.com/shorts/ShHuPrGvrlg
